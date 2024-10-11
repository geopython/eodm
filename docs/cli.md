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
* `transform`: Commands for various data and metadata...
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

* `stac_api`: Extract data from a STAC API
* `stac_catalog`: Extract data from a STAC Catalog

### `eodm extract stac_api`

Extract data from a STAC API

**Usage**:

```console
$ eodm extract stac_api [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `collections`
* `items`

#### `eodm extract stac_api collections`

**Usage**:

```console
$ eodm extract stac_api collections [OPTIONS] URL
```

**Arguments**:

* `URL`: [required]

**Options**:

* `--help`: Show this message and exit.

#### `eodm extract stac_api items`

**Usage**:

```console
$ eodm extract stac_api items [OPTIONS] URL COLLECTION
```

**Arguments**:

* `URL`: [required]
* `COLLECTION`: [required]

**Options**:

* `--bbox TEXT`
* `--datetime TEXT`
* `--help`: Show this message and exit.

### `eodm extract stac_catalog`

Extract data from a STAC Catalog

**Usage**:

```console
$ eodm extract stac_catalog [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `collection`
* `collections`
* `items`

#### `eodm extract stac_catalog collection`

**Usage**:

```console
$ eodm extract stac_catalog collection [OPTIONS] STAC_CATALOG_PATH COLLECTION_ID
```

**Arguments**:

* `STAC_CATALOG_PATH`: [required]
* `COLLECTION_ID`: [required]

**Options**:

* `--help`: Show this message and exit.

#### `eodm extract stac_catalog collections`

**Usage**:

```console
$ eodm extract stac_catalog collections [OPTIONS] STAC_CATALOG_PATH
```

**Arguments**:

* `STAC_CATALOG_PATH`: [required]

**Options**:

* `--help`: Show this message and exit.

#### `eodm extract stac_catalog items`

**Usage**:

```console
$ eodm extract stac_catalog items [OPTIONS] STAC_CATALOG_PATH [COLLECTION_ID]
```

**Arguments**:

* `STAC_CATALOG_PATH`: [required]
* `[COLLECTION_ID]`

**Options**:

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

* `stac_api`: Load metadata to a STAC API
* `stac_catalog`: Load data and metadata to a STAC catalog

### `eodm load stac_api`

Load metadata to a STAC API

**Usage**:

```console
$ eodm load stac_api [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `collection`
* `collections`
* `items`

#### `eodm load stac_api collection`

**Usage**:

```console
$ eodm load stac_api collection [OPTIONS] URL ID DESCRIPTION TITLE
```

**Arguments**:

* `URL`: [required]
* `ID`: [required]
* `DESCRIPTION`: [required]
* `TITLE`: [required]

**Options**:

* `--verify / --no-verify`: [default: verify]
* `--help`: Show this message and exit.

#### `eodm load stac_api collections`

**Usage**:

```console
$ eodm load stac_api collections [OPTIONS] URL COLLECTIONS
```

**Arguments**:

* `URL`: [required]
* `COLLECTIONS`: [required]

**Options**:

* `--verify / --no-verify`: [default: verify]
* `--help`: Show this message and exit.

#### `eodm load stac_api items`

**Usage**:

```console
$ eodm load stac_api items [OPTIONS] URL ITEMS
```

**Arguments**:

* `URL`: [required]
* `ITEMS`: [required]

**Options**:

* `--verify / --no-verify`: [default: verify]
* `--help`: Show this message and exit.

### `eodm load stac_catalog`

Load data and metadata to a STAC catalog

**Usage**:

```console
$ eodm load stac_catalog [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `catalog`
* `collection`

#### `eodm load stac_catalog catalog`

**Usage**:

```console
$ eodm load stac_catalog catalog [OPTIONS] BASE_PATH ID DESCRIPTION TITLE
```

**Arguments**:

* `BASE_PATH`: [required]
* `ID`: [required]
* `DESCRIPTION`: [required]
* `TITLE`: [required]

**Options**:

* `--help`: Show this message and exit.

#### `eodm load stac_catalog collection`

**Usage**:

```console
$ eodm load stac_catalog collection [OPTIONS] CATALOG_BASE_PATH ID DESCRIPTION TITLE
```

**Arguments**:

* `CATALOG_BASE_PATH`: [required]
* `ID`: [required]
* `DESCRIPTION`: [required]
* `TITLE`: [required]

**Options**:

* `--help`: Show this message and exit.

## `eodm transform`

Commands for various data and metadata transformations

**Usage**:

```console
$ eodm transform [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `data`
* `metadata`

### `eodm transform data`

**Usage**:

```console
$ eodm transform data [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `snowmap`

#### `eodm transform data snowmap`

**Usage**:

```console
$ eodm transform data snowmap [OPTIONS] ITEMS
```

**Arguments**:

* `ITEMS`: [required]

**Options**:

* `--bbox TEXT`
* `--green-band TEXT`: [default: green]
* `--swir-band TEXT`: [default: swir16]
* `--scl-band TEXT`: [default: scl]
* `--groupby TEXT`: [default: solar_day]
* `--help`: Show this message and exit.

### `eodm transform metadata`

**Usage**:

```console
$ eodm transform metadata [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `band-subset`
* `wrap-items`

#### `eodm transform metadata band-subset`

**Usage**:

```console
$ eodm transform metadata band-subset [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

#### `eodm transform metadata wrap-items`

**Usage**:

```console
$ eodm transform metadata wrap-items [OPTIONS] FILES OUTPUT_DIRECTORY COLLECTION
```

**Arguments**:

* `FILES`: [required]
* `OUTPUT_DIRECTORY`: [required]
* `COLLECTION`: [required]

**Options**:

* `--id TEXT`
* `--help`: Show this message and exit.

## `eodm version`

Prints software version

**Usage**:

```console
$ eodm version [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
