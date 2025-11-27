import pytest
from src.py_kata.list_multidimensional.tictactoe import winner

def test_winner_basic():
    assert winner([["X","O","O"],["X","O","O"],["X"," "," "]]) == "X wins"
    assert winner([["X","O","X"],["O","O","O"],[" "," ","X"]]) == "O wins"
    assert winner([["X","X","O"],["O","X","O"],["X","O","X"]]) == "X wins"
    assert winner([["O","X","X"],["O","X","O"],["X","O","X"]]) == "X wins"
    assert winner([["O","X","O"],["X","X","O"],["O","O","X"]]) == "Cat's game"
    assert winner([["O","X"," "],[" "," "," "],[" ","O"," "]]) == "Cat's game"
    assert winner([["O","X","X"],["X","X","O"],["X","O","X"]]) == "X is a cheater"

def test_winner_invalid():
    with pytest.raises(TypeError):
        winner(None)
    with pytest.raises(TypeError):
        winner("OXXOXOXXOX")
    with pytest.raises(ValueError):
        winner([["O","X","X"],["X","X","O"]])  # pas 3x3
    with pytest.raises(ValueError):
        winner([["O","X","X"],["X","X"],["X","O","X"]])  # pas 3x3
    with pytest.raises(ValueError):
        winner([["O","X","X"],["O","X","0"],["X","O","X"]])  # caractère illégal
