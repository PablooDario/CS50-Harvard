import fuel
import pytest

def test_ZeroDivision():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("0/0")
    assert fuel.convert("1/2") == 50

def test_xGreater():
    with pytest.raises(ValueError):
        fuel.convert("3/2")
    assert fuel.convert("2/3") == 67

def test_Gauge():
    assert fuel.gauge(1) == 'E'
    assert fuel.gauge(99) == 'F'
    assert fuel.gauge(50) == "50%"

def test_invalid_int():
    with pytest.raises(ValueError):
        fuel.convert("Dog")
    assert fuel.convert("1/2") == 50