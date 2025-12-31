from dlh.dag_utils import get_utils_version


def test_utils_version() -> None:
    assert get_utils_version() == "0.1.0"
