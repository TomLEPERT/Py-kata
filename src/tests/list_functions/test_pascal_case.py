from src.py_kata.list_functions.pascal_case import pascal_case

def test_pascal_case_basic():
    assert pascal_case("this is sparta") == "ThisIsSparta"
    assert pascal_case("sO rAdicAL DuDe") == "SoRadicalDude"

def test_pascal_case_no_mutation():
    original = "no mutation"
    result = pascal_case(original)
    assert original == "no mutation"
    assert result == "NoMutation"
