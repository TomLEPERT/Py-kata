
from src.py_kata.list_functions.censorship import censor

def test_censor_basic():
    sentences = [
        "I love the smell of tacos in the morning.",
        "Where is my umbrella?",
        "The test is not a diagnosis of the disease psittacosis.",
        "Eat tacos every day."
    ]
    forbidden = "tacos"
    expected = [
        "I love the smell of ***** in the morning.",
        "Where is my umbrella?",
        "The test is not a diagnosis of the disease psittacosis.",
        "Eat ***** every day."
    ]
    assert censor(sentences, forbidden) == expected

def test_censor_empty_and_single_word():
    assert censor([], "test") == []
    assert censor(["schnibble"], "schnibble") == ["*********"]

def test_censor_no_mutation():
    test_list = ["this test is awesome"]
    result = censor(test_list, "test")
    assert test_list == ["this test is awesome"]
    assert result == ["this **** is awesome"]

def test_censor_partial_words():
    sentences = ["testing tacos", "tacos are great"]
    assert censor(sentences, "tacos") == ["testing tacos", "***** are great"]
