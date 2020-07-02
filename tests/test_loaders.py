from papyrus.loaders import CBZLoader
from pytest import fixture


@fixture(scope="function")
def sample_contents():
    return [
        "000.jpg",
        "001.jpg",
        "002.jpg",
        "003.jpg",
        "004.jpg",
    ]


def test_load_cbz(sample_contents):
    loader = CBZLoader("samples/sample.cbz")

    for item in loader.get_pages_list():
        assert item in sample_contents
