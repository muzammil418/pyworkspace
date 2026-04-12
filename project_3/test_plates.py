from plates import is_valid

def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_start_letters():
    assert is_valid("1ABC") == False
    assert is_valid("AB") == True


def test_numbers_position():
    assert is_valid("ABC123") == True
    assert is_valid("AB12C3") == False


def test_zero_rule():
    assert is_valid("AB012") == False
    assert is_valid("AB123") == True


def test_special_characters():
    assert is_valid("AB@12") == False