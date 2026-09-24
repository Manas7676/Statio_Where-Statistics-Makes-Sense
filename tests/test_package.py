import statio


def test_package_version():
    assert hasattr(statio, "__version__")
    assert statio.__version__ == "0.1.0"