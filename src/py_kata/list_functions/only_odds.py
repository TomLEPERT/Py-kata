from typing import List

def odd(numbers: List[int]) -> List[int]:
    """
    Garde uniquement les valeurs impaires.
    Ne muter pas la liste originale et pas de boucle explicite.
    
    Ton code en dessous
    """
    
    
    
"""
Lancer le test : 
Dans le terminal se positioner dans le dossier src
Utiliser la commande : pytest tests/list_functions/test_only_odds.py -q

Aperçu du test : 

def test_odd_basic():
    assert odd([1, 2, 3, 4]) == [1, 3]
    assert odd([10, 20]) == []
    assert odd([]) == []

def test_odd_no_mutation():
    nums = [6, 7]
    result = odd(nums)
    assert nums == [6, 7]
    assert result == [7] if nums == [7] else result
"""