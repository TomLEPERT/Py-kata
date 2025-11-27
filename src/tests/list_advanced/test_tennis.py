import pytest
from src.py_kata.list_advanced.tennis import get_score

def test_basic_scores():
    assert get_score([1, 1, 1]) == "40-love"
    assert get_score([2, 1, 2, 2]) == "15-40"
    assert get_score([1, 2, 1, 2, 1, 2]) == "deuce"
    assert get_score([1, 1, 1, 2, 2, 2, 1]) == "ad in"

def test_invalid_arguments():
    with pytest.raises(TypeError):
        get_score(None)
    with pytest.raises(TypeError):
        get_score("abc")
    with pytest.raises(TypeError):
        get_score([1, 2, None])
    with pytest.raises(TypeError):
        get_score([1, 2, "a"])
    with pytest.raises(ValueError):
        get_score([0, 1])
    with pytest.raises(ValueError):
        get_score([1, 2, 3])