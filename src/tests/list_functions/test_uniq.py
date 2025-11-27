from src.py_kata.list_functions.uniq import uniq

def test_uniq_basic():
    assert uniq(["a", "a", "b", "b", "c", "a", "b", "c", "c"]) == ["a","b","c","a","b","c"]
    assert uniq(["a", "a", "a", "b", "b", "b", "c", "c", "c"]) == ["a","b","c"]
    assert uniq([]) == []
    assert uniq(["foo"]) == ["foo"]
    assert uniq(["bar", "bar", "bar", "bar", "bar"]) == ["bar"]
    assert uniq([None]) == [None]
    assert uniq([None, "a", "a"]) == [None, "a"]
    assert uniq([""]) == [""]

def test_uniq_no_mutation():
    test_list = ["a", "a", "b"]
    result = uniq(test_list)
    assert test_list == ["a", "a", "b"]
    assert result == ["a","b"]
