from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar = Jar(-2)
    jar = Jar(20)
    assert jar.capacity == 20


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.deposit(-2)
        jar.deposit(6)
    jar.deposit(5)
    assert jar.size == 5
    


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.withdraw(-1)
        jar.withdraw(6)
    jar.withdraw(2)
    assert jar.size == 3