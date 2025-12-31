from importlib.metadata import version, PackageNotFoundError


def get_utils_version() -> str:
    """Returns the version of the dag-utils package."""
    try:
        return version("dlh-dag-utils")
    except PackageNotFoundError:
        return "unknown"
