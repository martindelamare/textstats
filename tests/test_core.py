import pytest
from textstats import longest_word, word_count, char_frequencies

def test_longest_word_rejects_empty():
    with pytest.raises(ValueError):
        longest_word("")

@pytest.mark.parametrize("text,expected", [
    ("", 0), ("one", 1), ("the end.", 2)
])

def test_word_count(text, expected):
    assert word_count(text) == expected

@pytest.mark.parametrize("text,expected", [
    ("", {}), ("one", {"o" : 1, "n" : 1, "e" : 1}), ("the end.", {"t" : 1, "h" : 1, "e" : 2, "n" : 1, "d" : 1, "." : 1})
])

def test_char_frequencies(text, expected):
    assert char_frequencies(text) == expected

@pytest.mark.parametrize("text,expected", [
    ("I", "I"), ("one", "one"), ("the end.", "end.")
])

def test_longest_word(text, expected):
    assert longest_word(text) == expected