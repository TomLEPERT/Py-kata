from typing import Sequence

def social_like(names: Sequence[str]) -> str:
    """
    Renvoie le texte 'like' en anglais à la manière du kata:
    - [] -> "no one likes this"
    - ["Peter"] -> "Peter likes this"
    - ["Jacob", "Alex"] -> "Jacob and Alex like this"
    - ["Max","John","Mark"] -> "Max, John and Mark like this"
    - ["Alex","Jacob","Mark","Max"] -> "Alex, Jacob and 2 others like this"
    
    Ton code en dessous
    """




"""
Lancer le test : 
Dans le terminal se positioner dans le dossier src
Utiliser la commande : pytest tests/list/test_social_like.py -q

Aperçu du test : 

def test_social_like_various():
    assert social_like([]) == "no one likes this"
    assert social_like(["Peter"]) == "Peter likes this"
    assert social_like(["Jacob","Alex"]) == "Jacob and Alex like this"
    assert social_like(["Max","John","Mark"]) == "Max, John and Mark like this"
    assert social_like(["Alex","Jacob","Mark","Max"]) == "Alex, Jacob and 2 others like this"
    assert social_like(["A","B","C","D","E"]) == "A, B and 3 others like this"
"""



