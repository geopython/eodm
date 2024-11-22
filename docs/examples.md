# Examples

## Argo workflows

The following `Workflow` how a single run can be executed in argo workflows
with the `eodm` docker image. There are 4 steps that occur one after the other as is shown
by the `steps` configuration, and there are 4 templates that define how a container is
executed.

- `extract` step using the `extract` template runs first
- `transform` step using the `transform` template runs after the `extract` has finished and uses its output data
- `load-stac-catalog` step using the `load-stac-catalog` template runs after and uses data from `transform`
- `load-stac-api` as the last step using the `load-stac-api` template and runs after `load-stac-catalog` using its output data

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: band-subset-
spec:
  serviceAccountName: executor
  ttlStrategy:
    secondsAfterCompletion: 60
  artifactGC:
    strategy: OnWorkflowDeletion
    forceFinalizerRemoval: true
  podGC:
    strategy: OnWorkflowSuccess
    deleteDelayDuration: 20s
  entrypoint: band-subset
  templates:
  - name: extract
    container:
      image: eodm:latest
      imagePullPolicy: Never
      command: [sh, -c]
      args: ["eodm extract stac-api items https://earth-search.aws.element84.com/v1 sentinel-2-l2a --bbox=49.1,18.1,49.2,18.2 --datetime-interval=2023-06-01/2023-06-15 > /tmp/extractedItems"]
    outputs:
      artifacts:
      - name: extractedItems
        path: /tmp/extractedItems
        s3:
          key: extractedItems-{{workflow.uid}}
  - name: transform
    inputs:
      artifacts:
        - name: extractedItems
          path: /tmp/extractedItems
    outputs:
      artifacts:
      - name: transformedItems
        path: /tmp/transformedItems
        s3:
          key: transformedItems-{{workflow.uid}}
    container:
      image: eodm:latest
      imagePullPolicy: Never
      command: [sh, -c]
      args: ["eodm transform metadata band-subset red,green,blue,nir /tmp/extractedItems > /tmp/transformedItems"]
  - name: load-stac-catalog
    inputs:
      artifacts:
        - name: transformedItems
          path: /tmp/transformedItems
    outputs:
      artifacts:
        - name: loadedItems
          path: /tmp/loadedItems
          s3:
            key: loadedItems-{{workflow.uid}}
    container:
      image: eodm:latest
      imagePullPolicy: Never
      command: [sh, -c]
      args: ["eodm load stac-catalog items --target-profile gitlab s3://eox-gitlab-testdata/test/catalog.json /tmp/transformedItems > /tmp/loadedItems"]
      volumeMounts:
        - mountPath: /root/.aws/config
          name:  aws-config
          subPath: config
        - mountPath: /root/.aws/credentials
          name:  aws-secret
          subPath: credentials
    volumes:
      - configMap:
          name: aws
          items:
            - key: config
              path: config
        name: aws-config
      - secret:
          secretName: aws-secret
          items:
            - key: credentials
              path: credentials
        name: aws-secret
  - name: load-stac-api
    inputs:
      artifacts:
        - name: loadedItems
          path: /tmp/loadedItems
    container:
      image: eodm:latest
      imagePullPolicy: Never
      command: [sh, -c]
      args: ["eodm load stac-api items --no-verify --update https://minikube.local /tmp/loadedItems"]

  - name: band-subset
    steps:
      - - name: extract
          template: extract
      - - name: transform
          template: transform
          arguments:
            artifacts:
            - name: extractedItems
              from: "{{steps.extract.outputs.artifacts.extractedItems}}"
      - - name: load-stac-catalog
          template: load-stac-catalog
          arguments:
            artifacts:
            - name: transformedItems
              from: "{{steps.transform.outputs.artifacts.transformedItems}}"
      - - name: load-stac-api
          template: load-stac-api
          arguments:
            artifacts:
            - name: loadedItems
              from: "{{steps.load-stac-catalog.outputs.artifacts.loadedItems}}"
```

The next example shows how a `Workflow` can be scheduled using a `CronWorkflow` to
periodically load data from a STAC Catalog into a STAC API.

```yaml
apiVersion: argoproj.io/v1alpha1
kind: CronWorkflow
metadata:
  name: eodm-sync-items
spec:
  schedule: "*/5 * * * *"
  successfulJobsHistoryLimit: 3
  workflowSpec:
    serviceAccountName: executor
    podGC:
      strategy: OnWorkflowSuccess
      deleteDelayDuration: 20s
    entrypoint: eodm-sync
    templates:
    - name: extract
      container:
        image: eodm:latest
        imagePullPolicy: Never
        command: [sh, -c]
        args: ["eodm extract stac-catalog items s3://eox-gitlab-testdata/test/catalog.json > /tmp/extractedItems"]
        volumeMounts:
          - mountPath: /root/.aws/config
            name:  aws-config
            subPath: config
          - mountPath: /root/.aws/credentials
            name:  aws-secret
            subPath: credentials
      volumes:
        - configMap:
            name: aws
            items:
              - key: config
                path: config
          name: aws-config
        - secret:
            secretName: aws-secret
            items:
              - key: credentials
                path: credentials
          name: aws-secret
      outputs:
        artifacts:
        - name: extractedItems
          path: /tmp/extractedItems
    - name: load-stac-api
      inputs:
        artifacts:
          - name: extractedItems
            path: /tmp/extractedItems
      container:
        image: eodm:latest
        imagePullPolicy: Never
        command: [sh, -c]
        args: ["eodm load stac-api items --no-verify --update https://minikube.local /tmp/extractedItems"]


    - name: eodm-sync
      steps:
        - - name: extract
            template: extract
        - - name: load-stac-api
            template: load-stac-api
            arguments:
              artifacts:
              - name: extractedItems
                from: "{{steps.extract.outputs.artifacts.extractedItems}}"
```

The final example shows how to define a `WorkflowTemplate`. A `WorkflowTemplate` is a
blueprint of a task. `Workflow` runs are created from a `WorkflowTemplate` and they can
be parametrized, so a well defined pipeline can be ran with a wider array of options.

```yaml
apiVersion: argoproj.io/v1alpha1
kind: WorkflowTemplate
metadata:
  name: eodm-snowmap-generation
spec:
  serviceAccountName: executor
  ttlStrategy:
    secondsAfterCompletion: 86400
  entrypoint: snowmap
  volumeClaimTemplates:
  - metadata:
      name: workdir
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 2Gi
  arguments:
    parameters:
      - name: catalog_path
        value: s3://eox-gitlab-testdata/test/catalog.json
      - name: source_stac_url
        value: https://earth-search.aws.element84.com/v1
      - name: bbox
        value: 49.1,18.1,49.2,18.2
      - name: datetime_interval
        value: 2023-06-01/2023-06-15
      - name: destination_stac_url
        value: https://minikube.local
  templates:
  - name: extract
    container:
      image: eodm:latest
      imagePullPolicy: Never
      command: [sh, -c]
      args: ["eodm extract stac-api items {{inputs.parameters.source_stac_url}} sentinel-2-l2a --bbox={{inputs.parameters.bbox}} --datetime-interval={{inputs.parameters.datetime_interval}} > /tmp/extractedItems"]
    inputs:
      parameters:
      - name: source_stac_url
      - name: bbox
      - name: datetime_interval
    outputs:
      artifacts:
      - name: extractedItems
        path: /tmp/extractedItems
  - name: transform-snowmap
    inputs:
      artifacts:
        - name: extractedItems
          path: /tmp/extractedItems
    outputs:
      artifacts:
      - name: snowmapData
        path: /tmp/snowmapData
    container:
      image: eodm:latest
      imagePullPolicy: Never
      command: [sh, -c]
      args: ["eodm transform data snowmap --output-dir /data /tmp/extractedItems > /tmp/snowmapData"]
      volumeMounts:
      - name: workdir
        mountPath: /data/
  - name: transform-metadata
    inputs:
      artifacts:
        - name: snowmapData
          path: /tmp/snowmapData
    outputs:
      artifacts:
        - name: transformedItems
          path: /tmp/transformedItems
    container:
      image: eodm:latest
      imagePullPolicy: Never
      command: [sh, -c]
      args: ["eodm transform metadata wrap-items snowmap /data/snowmap_%Y%m%d_%H%M%S%f.tiff /tmp/snowmapData > /tmp/transformedItems"]
      volumeMounts:
      - name: workdir
        mountPath: /data/
  - name: load-stac-catalog
    inputs:
      parameters:
      - name: catalog_path
      artifacts:
        - name: transformedItems
          path: /tmp/transformedItems
    outputs:
      artifacts:
        - name: loadedItems
          path: /tmp/loadedItems
    container:
      image: eodm:latest
      imagePullPolicy: Never
      command: [sh, -c]
      args: ["eodm load stac-catalog items {{inputs.parameters.catalog_path}} /tmp/transformedItems > /tmp/loadedItems"]
      volumeMounts:
        - mountPath: /root/.aws/config
          name:  aws-config
          subPath: config
        - mountPath: /root/.aws/credentials
          name:  aws-secret
          subPath: credentials
        - name: workdir
          mountPath: /data/
    volumes:
      - configMap:
          name: aws
          items:
            - key: config
              path: config
        name: aws-config
      - secret:
          secretName: aws-secret
          items:
            - key: credentials
              path: credentials
        name: aws-secret
  - name: load-stac-api
    inputs:
      artifacts:
        - name: loadedItems
          path: /tmp/loadedItems
      parameters:
      - name: destination_stac_url
    container:
      image: eodm:latest
      imagePullPolicy: Never
      command: [sh, -c]
      args: ["eodm load stac-api items --update --no-verify {{inputs.parameters.destination_stac_url}} /tmp/loadedItems"]

  - name: snowmap
    steps:
      - - name: extract
          template: extract
          arguments:
            parameters:
            - name: source_stac_url
              value: "{{workflow.parameters.source_stac_url}}"
            - name: datetime_interval
              value: "{{workflow.parameters.datetime_interval}}"
            - name: bbox
              value: "{{workflow.parameters.bbox}}"
      - - name: transform-snowmap
          template: transform-snowmap
          arguments:
            artifacts:
            - name: extractedItems
              from: "{{steps.extract.outputs.artifacts.extractedItems}}"
      - - name: transform-metadata
          template: transform-metadata
          arguments:
            artifacts:
            - name: snowmapData
              from: "{{steps.transform-snowmap.outputs.artifacts.snowmapData}}"
      - - name: load-stac-catalog
          template: load-stac-catalog
          arguments:
            parameters:
            - name: catalog_path
              value: "{{workflow.parameters.catalog_path}}"
            artifacts:
            - name: transformedItems
              from: "{{steps.transform-metadata.outputs.artifacts.transformedItems}}"
      - - name: load-stac-api
          template: load-stac-api
          arguments:
            parameters:
            - name: destination_stac_url
              value: "{{workflow.parameters.destination_stac_url}}"
            artifacts:
            - name: loadedItems
              from: "{{steps.load-stac-catalog.outputs.artifacts.loadedItems}}"
```

For more information on argo workflows refer to the [documentation](https://argo-workflows.readthedocs.io/en/latest/)
