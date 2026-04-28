from seasons import calculate_minutes, convert_to_words
from datetime import date

def test_calculate_minutes():
    birth = date(2000, 1, 1)
    today = date(2000, 1, 2)
    assert calculate_minutes(birth, today) == 1440

def test_multiple_days():
    birth = date(2000, 1, 1)
    today = date(2000, 1, 11)
    assert calculate_minutes(birth, today) == 14400


def test_convert_to_words():
    assert convert_to_words(1440) == "one thousand four hundred forty"


def test_convert_to_words():
    result = convert_to_words(525600)
    assert "five hundred twenty-five thousand" in result.lower()