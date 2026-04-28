from numb3rs import validate
import pytest

def test_valid_ips():
    assert validate("192.168.1.1") == True
    assert validate("8.8.8.8") == True
    assert validate("0.0.0.0") == True


def test_invalid_range():
    assert validate("275.3.6.28") == False
    assert validate("256.256.256.256") == False


def test_invalid_format():
    assert validate("192.168.1") == False
    assert validate("192.168.1.1.1") == False


def test_non_numeric():
    assert validate("abc.def.ghi.jkl") == False
    assert validate("192.168.one.1") == False



