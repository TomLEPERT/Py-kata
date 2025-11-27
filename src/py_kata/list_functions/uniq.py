from typing import List
from itertools import groupby

def uniq(seq: List) -> List:
    """
    Supprime les doublons consécutifs.
    Ne muter pas la liste originale et pas de boucle explicite.
    
    Ton code en dessous
    """
    
    
"""
Lancer le test : 
Dans le terminal se positioner dans le dossier src
Utiliser la commande : pytest tests/list_functions/test_uniq.py -q

Aperçu du test : 

def test_uniq_basic():
    assert uniq(["a", "a", "b", "b", "c", "a", "b", "c", "c"]) == ["a","b","c","a","b","c"]
    assert uniq(["a", "a", "a", "b", "b", "b", "c", "c", "c"]) == ["a","b","c"]
    assert uniq([]) == []
    assert uniq(["foo"]) == ["foo"]
    assert uniq(["bar", "bar", "bar", "bar", "bar"]) == ["bar"]
    assert uniq([None]) == [None]
    assert uniq([None, "a", "a"]) == [None, "a"]
    assert uniq([""]) == [""]

def test_uniq_no_mutation():
    test_list = ["a", "a", "b"]
    result = uniq(test_list)
    assert test_list == ["a", "a", "b"]
    assert result == ["a","b"]
"""