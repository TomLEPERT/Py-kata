from typing import Iterable, List, Union

Number = Union[int, float]

def inverse_value(values: Iterable[Number]) -> List[Number]:
    """
    Renvoie une nouvelle liste où chaque nombre a son signe inversé.
    Exemple : [1, -2, 0] -> [-1, 2, 0]
    
    Ton code en dessous
    """




"""
Lancer le test : 
Dans le terminal se positioner dans le dossier src
Utiliser la commande : pytest tests/list/test_inverse_value.py -q

Aperçu du test : 

def test_inverse_basic():
    assert inverse_value([1, -2, 0, 5]) == [-1, 2, 0, -5]
    assert inverse_value([]) == []
    assert inverse_value([0]) == [0]

def test_inverse_types():
    assert inverse_value((1.5, -2.5)) == [-1.5, 2.5]
"""

