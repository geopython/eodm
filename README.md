# eodm - EO Data Mover

![build](https://github.com/geopython/eodm/actions/workflows/main.yml/badge.svg)

Library and CLI application for ETL (extract, transform, load) operations on EO data.

## Concept

Below are the main ideas on how to use the application. Note the shell piping operator,
the intended use case is such that output of one command is piped into the next. With this
a clear interface is required between the commands. For this purpose the
[STAC](https://stacspec.org/en) Item is chosen.

```shell
eodm extract stac-api items https://earth-search.aws.element84.com/v1 sentinel-2-l2a --bbox 49.1,18.1,49.2,18.2 --datetime-interval 2023-06-01/2023-06-30 \
| eodm transform metadata band-subset red,green,blue,nir \
| eodm load stac-catalog items s3://my-bucket/catalog.json \
| eodm load stac-api items https://stac2.hub-dev.eox.at/
```

```shell
eodm extract stac-catalog items s3://my-bucket/catalog.json \
| eodm load stac-api items https://stac2.hub-dev.eox.at/
```

There are also library functions which are thin wrappers around popular libraries,
with some custom implementations for certain sources.

## Current support

### Extract

### Transform

### Load
