from typing import Optional
import math

"""
    On vous donne un arbre binaire. Implémentez la fonction `sum` qui retourne la
    somme maximale le long d'un chemin allant de la racine à une feuille.

    Exemple :

        17
        /  \
    3   -10
    /    /  \
    2   16   1
            /
            13

    résultat : 23, puisque [17, -10, 16] est le chemin racine→feuille qui donne la somme maximale.

    Si le nœud racine est None, retourner 0.

    Cette fonction doit être récursive : vous ne pouvez pas utiliser de boucle.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


def sum(node: Optional[TreeNode]) -> int:





"""
    Lancer le test : 
    Dans le terminal se positioner dans le dossier src
    Utiliser la commande : pytest tests/binarytree/test_binarytree_sum.py -q

    Aperçu du test : 

    def test_sum_is_function():
        assert callable(sum)
        assert sum.__code__.co_argcount == 1


    def test_sum_is_recursive():
        source = sum.__code__.co_names
        # On vérifie qu'on voit "sum" dans le code OU qu'une fonction interne est récursive
        with open(sum.__code__.co_filename, "r") as f:
            code = f.read()
        assert "sum(" in code or "_max_root_to_leaf(" in code
        assert "for " not in code
        assert "while " not in code


    def test_sum_empty_tree():
        assert sum(None) == 0


    def test_sum_single_node():
        assert sum(TreeNode(42)) == 42


    def test_sum_given_example():
        Exemple : 
            17
            /  \
        3   -10
        /    /  \
        2   16   1
                    /
                13
        Résultat attendu = 23 via [17, -10, 16]
        tree = TreeNode(
            17,
            TreeNode(3, TreeNode(2)),
            TreeNode(
                -10,
                TreeNode(16),
                TreeNode(1, TreeNode(13))
            ),
        )
        assert sum(tree) == 23


    def test_sum_second_example():
            7
        /   \
        5     2
        \     \
            6     11
        / \
        1   9

        Chemin max = 7 + 5 + 6 + 9 = 27
        tree = TreeNode(
            7,
            TreeNode(
                5,
                None,
                TreeNode(
                    6,
                    TreeNode(1),
                    TreeNode(9)
                )
            ),
            TreeNode(2, None, TreeNode(11, TreeNode(4)))
        )
        assert sum(tree) == 27
"""