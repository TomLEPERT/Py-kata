from src.py_kata.list.found_min import found_min

def test_found_min_value():
    assert found_min([3, 1, 4, 1, 5]) == 1
    assert found_min([-2, -5, 0, 7]) == -5
    assert found_min([10]) == 10
    assert found_min((2.5, 0.1, 2.49)) == 0.1

def test_found_min_empty():
    assert found_min([]) is None
    assert found_min(()) is None

def test_found_min_with_duplicates():
    assert found_min([2,2,2]) == 2