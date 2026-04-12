from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"

    def test_uppercase():
        assert shorten("TWITTER") == "TWTTR"

    def test_mixed_case():
        assert shorten("TwItTeR") == "twTtR"

    def test_no_vowels():
        assert shorten("twitter") == ""

    def test_only_vowels():
        assert shorten("aeiou") == ""

    def test_number_symbol():
        assert shorten("123!") == "123!"


