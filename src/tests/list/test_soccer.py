from src.py_kata.list.soccer import soccer

def test_soccer_basic():
    matches = ["3:1", "2:2", "0:1", "4:4", "5:0"]
    # 3:1 -> 3, 2:2 -> 1, 0:1 -> 0, 4:4 -> 1, 5:0 -> 3 => total = 8
    assert soccer(matches) == 8

def test_soccer_spaces_and_order():
    assert soccer([" 1:0 ", "0:0", "2:3"]) == 4  # 3 + 1 + 0
    assert soccer([]) == 0

def test_soccer_all_losses():
    assert soccer(["0:1", "0:2", "1:4"]) == 0
