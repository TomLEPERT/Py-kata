import pytest
from src.py_kata.list_multidimensional.minesweeper import sweep

def test_sweep_basic():
    grid = [
        [0,0,0,1],
        [0,1,0,0],
        [1,0,0,0]
    ]
    assert sweep(grid,1,1) == "kaboom"
    assert sweep(grid,0,3) == "kaboom"
    assert sweep(grid,2,0) == "kaboom"
    assert sweep(grid,0,0) == 1
    assert sweep(grid,1,2) == 2
    assert sweep(grid,2,3) == 0

def test_sweep_invalid():
    grid = [[0]]
    with pytest.raises(TypeError):
        sweep(None, 1, 1)
    with pytest.raises(TypeError):
        sweep("a",1,1)
    with pytest.raises(TypeError):
        sweep([[0,"0"]],0,0)
    with pytest.raises(ValueError):
        sweep([[0]],-1,0)
    with pytest.raises(ValueError):
        sweep([[0]],0,1)
