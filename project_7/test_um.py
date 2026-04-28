from um import count

def teat_basic():
    assert count("um")  == 1


def test_multiple():
    assert count("um, um, um") == 3

def test_case_insensitive():
    assert count("Um, um, UM") == 3

def test_not_substring():
    assert count("yummy") == 0


def test_mixed():
    assert count("Hello, um, world") == 1


def test_with_punctuation():
    assert count("um? um! um.") == 3
