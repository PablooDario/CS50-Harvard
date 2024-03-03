from bank import value

def test_hello():
    assert value("Hello") == 0

def test_starts_h():
    assert value("How you doing?") == 20

def test_no_h():
    assert value("What's happening?") == 100
