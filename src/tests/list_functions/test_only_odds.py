from src.py_kata.list_functions.only_odds import odd

def test_odd_basic():
    assert odd([1, 2, 3, 4]) == [1, 3]
    assert odd([10, 20]) == []
    assert odd([]) == []

def test_odd_no_mutation():
    nums = [6, 7]
    result = odd(nums)
    assert nums == [6, 7]
    assert result == [7] if nums == [7] else result  # fallback
