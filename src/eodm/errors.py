class ExtractError(Exception):
    """Raised when an error occurs while extracting"""

    pass


class LoadError(Exception):
    """Raised when an error occurs while loading"""

    pass


class TransformError(Exception):
    """Raised when an error occurs while transforming"""

    pass
