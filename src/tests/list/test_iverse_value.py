from src.py_kata.list.inverse_value import inverse_value

def test_inverse_basic():
    assert inverse_value([1, -2, 0, 5]) == [-1, 2, 0, -5]
    assert inverse_value([]) == []
    assert inverse_value([0]) == [0]

def test_inverse_types():
    assert inverse_value((1.5, -2.5)) == [-1.5, 2.5]
