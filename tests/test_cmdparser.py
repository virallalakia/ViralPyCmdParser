from viralpycmdparser import cmdparser


def test_hello_world():
    assert cmdparser.hello_world() == "Hello World"
