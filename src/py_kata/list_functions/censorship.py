from typing import List
import re

def censor(sentences: List[str], forbidden: str) -> List[str]:
    """
    Remplace le mot forbidden par des étoiles dans chaque phrase.
    
    - Ne modifie pas la liste originale
    - Ne censurise que le mot complet
    - Pas de boucle explicite
    
    Ton code en dessous
    """
    
    


"""
Lancer le test : 
Dans le terminal se positioner dans le dossier src
Utiliser la commande : pytest tests/list_functions/test_censorship.py -q

Aperçu du test : 

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
"""

