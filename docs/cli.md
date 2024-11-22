# `eodm`

**Usage**:

```console
$ eodm [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `extract`: Commands for extracting data from various...
* `load`: Commands for loading data into various...
* `transform`: Commands for data and metadata...
* `version`: Prints software version

## `eodm extract`

Commands for extracting data from various sources

**Usage**:

```console
$ eodm extract [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `openeo`: Extract data from openEO results
* `stac-api`: Extract data from a STAC API
* `stac-catalog`: Extract data from a STAC Catalog

### `eodm extract openeo`

Extract data from openEO results

**Usage**:

```console
$ eodm extract openeo [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `results`

#### `eodm extract openeo results`

**Usage**:

```console
$ eodm extract openeo results [OPTIONS] ASSET_NAME [RESULTS]
```

**Arguments**:

* `ASSET_NAME`: [required]
* `[RESULTS]`: [default: <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>]

**Options**:

* `--help`: Show this message and exit.

### `eodm extract stac-api`

Extract data from a STAC API

**Usage**:

```console
$ eodm extract stac-api [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `collections`: Extract all collections from STAC API
* `items`: Extract items from a collection found in a...

#### `eodm extract stac-api collections`

Extract all collections from STAC API

**Usage**:

```console
$ eodm extract stac-api collections [OPTIONS] URL
```

**Arguments**:

* `URL`: [required]

**Options**:

* `-o, --output [default|json]`: Output format. Default to STDOUT multiline  [default: default]
* `--help`: Show this message and exit.

#### `eodm extract stac-api items`

Extract items from a collection found in a STAC API

**Usage**:

```console
$ eodm extract stac-api items [OPTIONS] URL COLLECTION
```

**Arguments**:

* `URL`: [required]
* `COLLECTION`: [required]

**Options**:

* `-b, --bbox BBOX`: WGS 84 format:minx,miny,maxx,maxy  [default: -180.0,-90.0,180.0, 90.0]
* `-d, --datetime-interval DATETIME_INTERVAL`: ISO format: single, start/end, start/.., ../end for open bounds  [default: 1900-01-01 00:00:00/..]
* `-l, --limit INT`: Limit query.  [default: 0]
* `-o, --output [default|json]`: Output format. Default to STDOUT multiline  [default: default]
* `--help`: Show this message and exit.

### `eodm extract stac-catalog`

Extract data from a STAC Catalog

**Usage**:

```console
$ eodm extract stac-catalog [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `collection`: Extract a collection from a STAC Catalog
* `collections`: Extract collections from a STAC Catalog
* `items`: Extract items from a STAC Catalog

#### `eodm extract stac-catalog collection`

Extract a collection from a STAC Catalog

**Usage**:

```console
$ eodm extract stac-catalog collection [OPTIONS] STAC_CATALOG_PATH COLLECTION_ID
```

**Arguments**:

* `STAC_CATALOG_PATH`: [required]
* `COLLECTION_ID`: [required]

**Options**:

* `--help`: Show this message and exit.

#### `eodm extract stac-catalog collections`

Extract collections from a STAC Catalog

**Usage**:

```console
$ eodm extract stac-catalog collections [OPTIONS] STAC_CATALOG_PATH
```

**Arguments**:

* `STAC_CATALOG_PATH`: [required]

**Options**:

* `--help`: Show this message and exit.

#### `eodm extract stac-catalog items`

Extract items from a STAC Catalog

**Usage**:

```console
$ eodm extract stac-catalog items [OPTIONS] STAC_CATALOG_PATH
```

**Arguments**:

* `STAC_CATALOG_PATH`: [required]

**Options**:

* `--collection-id TEXT`
* `--help`: Show this message and exit.

## `eodm load`

Commands for loading data into various destinations

**Usage**:

```console
$ eodm load [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `stac-api`: Load metadata to a STAC API
* `stac-catalog`: Load data and metadata to a STAC catalog

### `eodm load stac-api`

Load metadata to a STAC API

**Usage**:

```console
$ eodm load stac-api [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `collection`: Create and load a single collection to a...
* `collections`: Load multiple collections to a stac API.
* `items`: Load multiple items into a STAC API

#### `eodm load stac-api collection`

Create and load a single collection to a STAC API.

**Usage**:

```console
$ eodm load stac-api collection [OPTIONS] URL ID DESCRIPTION TITLE
```

**Arguments**:

* `URL`: [required]
* `ID`: [required]
* `DESCRIPTION`: [required]
* `TITLE`: [required]

**Options**:

* `--verify / --no-verify`: [default: verify]
* `--update / --no-update`: [default: no-update]
* `--help`: Show this message and exit.

#### `eodm load stac-api collections`

Load multiple collections to a stac API. Collections can be piped from STDIN or a file
with Collection jsons on each line

**Usage**:

```console
$ eodm load stac-api collections [OPTIONS] URL [COLLECTIONS]
```

**Arguments**:

* `URL`: [required]
* `[COLLECTIONS]`: [default: <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>]

**Options**:

* `--verify / --no-verify`: [default: verify]
* `--update / --no-update`: [default: no-update]
* `--skip-existing / --no-skip-existing`: [default: no-skip-existing]
* `-o, --output [default|json]`: Output format. Default to STDOUT multiline  [default: default]
* `--help`: Show this message and exit.

#### `eodm load stac-api items`

Load multiple items into a STAC API

**Usage**:

```console
$ eodm load stac-api items [OPTIONS] URL [ITEMS]
```

**Arguments**:

* `URL`: [required]
* `[ITEMS]`: [default: <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>]

**Options**:

* `--verify / --no-verify`: [default: verify]
* `--update / --no-update`: [default: no-update]
* `--skip-existing / --no-skip-existing`: [default: no-skip-existing]
* `-o, --output [default|json]`: Output format. Default to STDOUT multiline  [default: default]
* `--help`: Show this message and exit.

### `eodm load stac-catalog`

Load data and metadata to a STAC catalog

**Usage**:

```console
$ eodm load stac-catalog [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `catalog`: Create a STAC Catalog
* `collection`: Create and add a STAC Collection to an...
* `collections`: Load STAC Collections to an existing STAC...
* `items`: Load STAC Items to an existing STAC Catalog.

#### `eodm load stac-catalog catalog`

Create a STAC Catalog

**Usage**:

```console
$ eodm load stac-catalog catalog [OPTIONS] CATALOG_PATH ID DESCRIPTION TITLE
```

**Arguments**:

* `CATALOG_PATH`: [required]
* `ID`: [required]
* `DESCRIPTION`: [required]
* `TITLE`: [required]

**Options**:

* `--help`: Show this message and exit.

#### `eodm load stac-catalog collection`

Create and add a STAC Collection to an existing STAC Catalog

**Usage**:

```console
$ eodm load stac-catalog collection [OPTIONS] CATALOG_PATH ID DESCRIPTION TITLE
```

**Arguments**:

* `CATALOG_PATH`: [required]
* `ID`: [required]
* `DESCRIPTION`: [required]
* `TITLE`: [required]

**Options**:

* `--help`: Show this message and exit.

#### `eodm load stac-catalog collections`

Load STAC Collections to an existing STAC Catalog

**Usage**:

```console
$ eodm load stac-catalog collections [OPTIONS] CATALOG_PATH [COLLECTIONS]
```

**Arguments**:

* `CATALOG_PATH`: [required]
* `[COLLECTIONS]`: [default: <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>]

**Options**:

* `--help`: Show this message and exit.

#### `eodm load stac-catalog items`

Load STAC Items to an existing STAC Catalog. Each item will be sorted to its
collection

**Usage**:

```console
$ eodm load stac-catalog items [OPTIONS] CATALOG_PATH [ITEMS]
```

**Arguments**:

* `CATALOG_PATH`: [required]
* `[ITEMS]`: [default: <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>]

**Options**:

* `--source-profile TEXT`
* `--target-profile TEXT`
* `--chunk-size INTEGER`: [default: 100000]
* `--help`: Show this message and exit.

## `eodm transform`

Commands for data and metadata transformations

**Usage**:

```console
$ eodm transform [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `data`: Commands for data transformations
* `metadata`: Commands for metadata transformations

### `eodm transform data`

Commands for data transformations

**Usage**:

```console
$ eodm transform data [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `ensure-cog`: Creates COG images from all assets in ITEMS
* `snowmap`: Creates snowmap images from ITEMS

#### `eodm transform data ensure-cog`

Creates COG images from all assets in ITEMS

**Usage**:

```console
$ eodm transform data ensure-cog [OPTIONS] [ITEMS]
```

**Arguments**:

* `[ITEMS]`: [default: <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>]

**Options**:

* `--overview-level INTEGER`: [default: 3]
* `--output-dir TEXT`: [default: /tmp]
* `--help`: Show this message and exit.

#### `eodm transform data snowmap`

Creates snowmap images from ITEMS

**Usage**:

```console
$ eodm transform data snowmap [OPTIONS] [ITEMS]
```

**Arguments**:

* `[ITEMS]`: [default: <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>]

**Options**:

* `-b, --bbox BBOX`: WGS 84 format:minx,miny,maxx,maxy  [default: -180.0,-90.0,180.0, 90.0]
* `--green-band TEXT`: [default: green]
* `--swir-band TEXT`: [default: swir16]
* `--scl-band TEXT`: [default: scl]
* `--groupby TEXT`: [default: solar_day]
* `--output-dir TEXT`: [default: /tmp]
* `--help`: Show this message and exit.

### `eodm transform metadata`

Commands for metadata transformations

**Usage**:

```console
$ eodm transform metadata [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `band-subset`: Subsets provided STAC ITEMS to only...
* `wrap-items`: Wrap FILES in STAC items using...

#### `eodm transform metadata band-subset`

Subsets provided STAC ITEMS to only include the specified BANDS

**Usage**:

```console
$ eodm transform metadata band-subset [OPTIONS] BANDS [ITEMS]
```

**Arguments**:

* `BANDS`: Comma separated list of bands  [required]
* `[ITEMS]`: [default: <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>]

**Options**:

* `--help`: Show this message and exit.

#### `eodm transform metadata wrap-items`

Wrap FILES in STAC items using STRPTIME_FORMAT to extract the date and assign to COLLECTION

**Usage**:

```console
$ eodm transform metadata wrap-items [OPTIONS] COLLECTION STRPTIME_FORMAT [FILES]
```

**Arguments**:

* `COLLECTION`: [required]
* `STRPTIME_FORMAT`: [required]
* `[FILES]`: [default: <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>]

**Options**:

* `--help`: Show this message and exit.

## `eodm version`

Prints software version

**Usage**:

```console
$ eodm version [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
