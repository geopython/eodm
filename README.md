# eodm - EO Data Mover

Package and CLI application used to perform ETL operations on EO data.

## Usage

Below are example uses of the CLI application. Note the shell piping operator, the intended
use case is such that output of one command is piped into the next. With this a clear interface
is required between the commands. For this purpose the [STAC](https://stacspec.org/en) Item is chosen.

```shell
eodm extract stac_api items https://earth-search.aws.element84.com/v1 sentinel-2-l2a --bbox 49.1,18.1,49.2,18.2 --datetime-interval 2023-06-01/2023-06-30 \
| eodm transform metadata band-subset red,green,blue,nir \
| eodm load stac_catalog items s3://eox-gitlab-testdata/vs/catalog.json \
| eodm load stac_api items https://stac2.hub-dev.eox.at/
```

```shell
eodm extract stac_api items https://earth-search.aws.element84.com/v1 sentinel-2-l2a --bbox 49.1,18.1,49.2,18.2 --datetime-interval 2023-06-01/2023-06-30 \
| eodm transform data snowmap \
| eodm transform metadata wrap-items snowmap "/tmp/snowmap_%Y%m%d_%H%M%S%f.tiff" \
| eodm load stac_catalog items s3://gtif-data/test/catalog.json \
| eodm load stac_api items --no-verify https://minikube.local
```

```shell
eodm extract stac_catalog items s3://eox-gitlab-testdata/vs/catalog.json \
| eodm load stac_api items https://stac2.hub-dev.eox.at/
```

```shell
eodm extract openeo /home/nikola/Testground/geo/openeo-tests/results_1_openeo_vito/job-results.json\
| eodm transform data ensure_cog \
| eodm transform metadata wrap-items openeo "/tmp/openEO_%Y-%m-%dZ.tif" \
| eodm load stac_catalog items s3://gtif-data/test/catalog.json \
| eodm load stac_api items https://stac2.hub-dev.eox.at/
```

```shell
eodm extract stac_api items https://earth-search.aws.element84.com/v1 sentinel-2-l2a --bbox 49.1,18.1,49.2,18.2 --datetime-interval 2023-06-01/2023-06-30\
| eodm transform metadata band-subset red,green,blue,nir
```
