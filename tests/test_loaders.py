from papyrus.loaders import CBZLoader


def test_load_cbz():
    loader = CBZLoader()
    hq = loader("sample/sample.cbz")
    for item in hq.list_contents():
        assert item in ["000.jpg", "001.jpg", "002.jpg", "003.jpg", "004.jpg"]
