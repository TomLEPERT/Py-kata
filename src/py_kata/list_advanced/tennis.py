from typing import List

def get_score(points: List[int]) -> str:
    """
    Retourne le score actuel d'un jeu de tennis en fonction d'une liste de points.
    
    Règles :
    - 0, 1, 2, 3 points : "love", "15", "30", "40"
    - Si au moins 3 points pour chaque joueur :
        * égalité -> "deuce"
        * un joueur a 1 point de plus -> "ad in" ou "ad out"
        
    Ton code en dessous
    """
    
    

"""
Lancer le test : 
Dans le terminal se positioner dans le dossier src
Utiliser la commande : pytest tests/list_advanced/test_tennis.py -q

Aperçu du test : 
def test_basic_scores():
    assert get_score([1, 1, 1]) == "40-love"
    assert get_score([2, 1, 2, 2]) == "15-40"
    assert get_score([1, 2, 1, 2, 1, 2]) == "deuce"
    assert get_score([1, 1, 1, 2, 2, 2, 1]) == "ad in"

def test_invalid_arguments():
    with pytest.raises(TypeError):
        get_score(None)
    with pytest.raises(TypeError):
        get_score("abc")
    with pytest.raises(TypeError):
        get_score([1, 2, None])
    with pytest.raises(TypeError):
        get_score([1, 2, "a"])
    with pytest.raises(ValueError):
        get_score([0, 1])
    with pytest.raises(ValueError):
        get_score([1, 2, 3])
"""