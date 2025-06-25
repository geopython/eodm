## 0.1.0 (2025-06-25)

### Feat

- ogcapi harvesting
- added id as output type
- skip collection
- added with_env to main grouping
- added update flag and made load more idempotent
- added some relevant filters for odata
- added odata implementation
- added support for basic authentication for load operations
- added typer entrypoint pluggability
- added opensearch harvesting
- added query and feature to extract
- added load features
- added limit
- added extract concept
- added encoder concept

### Fix

- removed cql for now
- ignore error for now until used
- updated handling of protocol
- lint
- flow in item handling
- improved filesystem handling
- added source profile to load
- added output serialization
- assignment of asset href fix
- fixed wrong band list given
- used odata mock
- polygon and odata nextlink
- added annotation for odataproduct
- update type annotations for Typer compatibility
- fixed imports
- allowed any geometry instead of long union
- fixed type
- fixed import
- moved logic to cli for printing
- fixed import
- bbox iter from methods
- export correct types

### Refactor

- resetting defaults
- updated names for parsers
- naming & docs
- moved to more recent construct
- reorganized modules
- **cli_folder**: organized cli functions to separate directory
