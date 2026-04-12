from fuel import convert, gauge
import pytest


def test_convert_normal():
    assert convert("1/2") == 50
    assert convert("1/4") == 25


def test_convert_edge():
    assert convert("0/1") == 0
    assert convert("1/1") == 100


def test_convert_errors():
    with pytest.raises(ValueError):
        convert("2/1")   # X > Y

    with pytest.raises(ZeroDivisionError):
        convert("1/0")

    with pytest.raises(ValueError):
        convert("a/b")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"