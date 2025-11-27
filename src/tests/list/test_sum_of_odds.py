from src.py_kata.list.sum_of_odds import sum_of_odds

def test_sum_of_odds_basic():
    assert sum_of_odds([1,2,3,4,5]) == 1+3+5
    assert sum_of_odds([]) == 0
    assert sum_of_odds([2,4,6]) == 0
    assert sum_of_odds([-3, -2, -1, 0, 1]) == -3 + -1 + 1