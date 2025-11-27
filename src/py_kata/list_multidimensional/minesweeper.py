from typing import List

def sweep(grid: List[List[int]], row: int, column: int):
    """
    Fonction `sweep` pour le jeu Démineur.

    Paramètres :
    - grid : une matrice représentant le plateau de démineur, où 0 représente une case vide et 1 une bombe.
            La largeur et la hauteur de la grille peuvent varier.
    - row : la coordonnée verticale (ligne) de la case à vérifier.
    - column : la coordonnée horizontale (colonne) de la case à vérifier.

    Retourne :
    - "kaboom" si la case contient une bombe.
    - le nombre de bombes adjacentes si la case est vide.

    Exceptions levées :
    - TypeError si grid est None ou n'est pas une liste.
    - TypeError si au moins une valeur de la grille n'est pas 0 ou 1.
    - TypeError si row ou column sont None ou ne sont pas des entiers.
    - ValueError si la largeur ou la hauteur de la grille est inférieure à 1.
    - ValueError si row ou column sont hors des limites de la grille.

    Exemple :

    grid = [
    [0, 0, 0, 1],
    [0, 1, 0, 0],
    [1, 0, 0, 0]
    ]
    row = 1
    column = 2

    résultat : 2
    
    Ton code en dessous
    """




"""
Lancer le test : 
Dans le terminal se positioner dans le dossier src
Utiliser la commande : pytest tests/list_multidimensional/test_minesweeper.py -q

Aperçu du test : 

def test_sweep_basic():
    grid = [
        [0,0,0,1],
        [0,1,0,0],
        [1,0,0,0]
    ]
    assert sweep(grid,1,1) == "kaboom"
    assert sweep(grid,0,3) == "kaboom"
    assert sweep(grid,2,0) == "kaboom"
    assert sweep(grid,0,0) == 1
    assert sweep(grid,1,2) == 2
    assert sweep(grid,2,3) == 0

def test_sweep_invalid():
    grid = [[0]]
    with pytest.raises(TypeError):
        sweep(None, 1, 1)
    with pytest.raises(TypeError):
        sweep("a",1,1)
    with pytest.raises(TypeError):
        sweep([[0,"0"]],0,0)
    with pytest.raises(ValueError):
        sweep([[0]],-1,0)
    with pytest.raises(ValueError):
        sweep([[0]],0,1)
"""