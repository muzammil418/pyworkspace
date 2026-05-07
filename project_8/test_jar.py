import pytest
from jar import Jar

def test_init():
    jar = Jar(11)
    assert jar.capacity == 11
    assert jar.size == 0


def test_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-1)

    with pytest.raises(ValueError):
        Jar("abc")


def test_str():
    jar = Jar(5)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.deposit(3)  


def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.withdraw(5)  


def test_negative_values():
    jar = Jar(5)

    with pytest.raises(ValueError):
        jar.deposit(-1)

    with pytest.raises(ValueError):
        jar.withdraw(-1)