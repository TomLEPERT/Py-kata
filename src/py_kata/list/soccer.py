from typing import Iterable

def soccer(results: Iterable[str]) -> int:
    """
    results: iterable de chaînes "x:y" (x et y entiers).
    Pour chaque match :
     - si x > y : +3 points
     - si x == y: +1 point
     - sinon: 0
    Retourne le total.
    
    Ton code en dessous
    """



"""
Lancer le test : 
Dans le terminal se positioner dans le dossier src
Utiliser la commande : pytest tests/list/test_soccer.py -q

Aperçu du test : 

def test_soccer_basic():
    matches = ["3:1", "2:2", "0:1", "4:4", "5:0"]
    # 3:1 -> 3, 2:2 -> 1, 0:1 -> 0, 4:4 -> 1, 5:0 -> 3 => total = 8
    assert soccer(matches) == 8

def test_soccer_spaces_and_order():
    assert soccer([" 1:0 ", "0:0", "2:3"]) == 4  # 3 + 1 + 0
    assert soccer([]) == 0

def test_soccer_all_losses():
    assert soccer(["0:1", "0:2", "1:4"]) == 0
"""