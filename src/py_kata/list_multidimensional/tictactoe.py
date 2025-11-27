from typing import List

def winner(grid: List[List[str]]) -> str:
    """
    Analyse une grille 3x3 de Tic-Tac-Toe et retourne le résultat.

    Paramètres :
    - grid : liste 3x3 représentant la grille
        "X" : joueur X
        "O" : joueur O
        " " : case vide

    Retourne :
    - "X wins" si X a gagné
    - "O wins" si O a gagné
    - "Cat's game" si égalité ou personne ne gagne
    - "{player} is a cheater" si le joueur a triché (plus de différence de 1 point entre X et O)

    Exceptions levées :
    - TypeError si grid est None ou n'est pas une liste
    - ValueError si la taille de la grille n'est pas 3x3
    - ValueError avec le texte "Illegal character" si la grille contient un caractère invalide
    """
    
    
    
"""
Lancer le test : 
Dans le terminal se positioner dans le dossier src
Utiliser la commande : pytest tests/list_multidimensional/test_tictactoe.py -q

Aperçu du test : 

def test_winner_basic():
    assert winner([["X","O","O"],["X","O","O"],["X"," "," "]]) == "X wins"
    assert winner([["X","O","X"],["O","O","O"],[" "," ","X"]]) == "O wins"
    assert winner([["X","X","O"],["O","X","O"],["X","O","X"]]) == "X wins"
    assert winner([["O","X","X"],["O","X","O"],["X","O","X"]]) == "X wins"
    assert winner([["O","X","O"],["X","X","O"],["O","O","X"]]) == "Cat's game"
    assert winner([["O","X"," "],[" "," "," "],[" ","O"," "]]) == "Cat's game"
    assert winner([["O","X","X"],["X","X","O"],["X","O","X"]]) == "X is a cheater"

def test_winner_invalid():
    with pytest.raises(TypeError):
        winner(None)
    with pytest.raises(TypeError):
        winner("OXXOXOXXOX")
    with pytest.raises(ValueError):
        winner([["O","X","X"],["X","X","O"]])  # pas 3x3
    with pytest.raises(ValueError):
        winner([["O","X","X"],["X","X"],["X","O","X"]])  # pas 3x3
    with pytest.raises(ValueError):
        winner([["O","X","X"],["O","X","0"],["X","O","X"]])  # caractère illégal
"""