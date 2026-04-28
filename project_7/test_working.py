from working import convert
import pytest


def test_basic():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_with_minutes():
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"


def test_mixed():
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"


def test_midnight():
    assert convert("12 AM to 1 AM") == "00:00 to 01:00"


def test_noon():
    assert convert("11 AM to 12 PM") == "11:00 to 12:00"


def test_wrap_around():
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"


def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")


def test_invalid_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")


def test_missing_to():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")