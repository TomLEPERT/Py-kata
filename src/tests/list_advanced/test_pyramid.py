import pytest
from src.py_kata.list_advanced.pyramid import build

def test_basic_pyramid():
    assert build(1) == ["*"]
    assert build(2) == [" * ", "***"]
    assert build(5) == [
        "    *    ",
        "   ***   ",
        "  *****  ",
        " ******* ",
        "*********",
    ]

def test_invalid_values():
    import builtins
    with pytest.raises(ValueError):
        build(0)
    with pytest.raises(ValueError):
        build(-1)
    with pytest.raises(TypeError):
        build(None)
    with pytest.raises(TypeError):
        build("a")