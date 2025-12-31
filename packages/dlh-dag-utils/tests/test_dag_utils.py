from importlib.metadata import version
from dlh.dag_utils import get_utils_version


def test_utils_version() -> None:
    # Verify that the function returns the same version as importlib.metadata
    installed_version = version("dlh-dag-utils")
    assert get_utils_version() == installed_version
    # Verify it is not unknown in the test environment
    assert get_utils_version() != "unknown"
