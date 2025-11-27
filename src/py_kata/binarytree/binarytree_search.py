from typing import Optional    
"""
    Un arbre binaire de recherche (BST) est un arbre binaire avec ces propriétés :
    * le sous-arbre gauche d'un nœud contient uniquement des nœuds dont la clé est inférieure à la clé du nœud
    * le sous-arbre droit d'un nœud contient uniquement des nœuds dont la clé est supérieure à la clé du nœud
    * les sous-arbres gauche et droit doivent eux-mêmes être des BST. Il ne doit pas y avoir de doublons.

    Exemple :

            8
        /   \
        3     10
        / \      \
    1   6      14
        / \    /
        4   7  13

    Implémentez la fonction `search` qui, étant donné un BST et une valeur :
    * retourne le nœud où la valeur est trouvée
    * retourne None si la valeur n'existe pas dans l'arbre

    Cette fonction doit être récursive : vous ne pouvez pas utiliser de boucle.
"""

class TreeNode:
    def __init__(self, value, left=None, right=None):
        """
        Représente un nœud d'un arbre binaire de recherche.
        value : clé entière du nœud
        left  : sous-arbre gauche (ou None)
        right : sous-arbre droit (ou None)
        """
        self.value = value
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right

def search(node: Optional[TreeNode], value: int) -> Optional[TreeNode]:
    """
    Recherche récursive d'une valeur dans un Binary Search Tree.

    - Retourne le TreeNode contenant la valeur si trouvé.
    - Retourne None si node est None ou si la valeur n'existe pas.
    - Doit être implémentée récursivement (pas de boucle).
    """




"""
Lancer le test : 
Dans le terminal se positioner dans le dossier src
Utiliser la commande : pytest tests/binarytree/test_binarytree_search.py -q

Aperçu du test : 

def make_tree():
    Construit l'arbre de l'exemple :
            8
          /   \
         3     10
        / \      \
       1   6      14
          / \    /
         4   7  13
    return TreeNode(
        8,
        TreeNode(
            3,
            TreeNode(1),
            TreeNode(6, TreeNode(4), TreeNode(7))
        ),
        TreeNode(10, None, TreeNode(14, TreeNode(13), None))
    )

    def test_search_none_tree():
        assert search(None, 3) is None

    def test_search_not_found_and_found():
        tree = make_tree()
        assert search(tree, 42) is None

        node6 = search(tree, 6)
        assert node6 is not None and node6.value == 6

        node13 = search(tree, 13)
        assert node13 is not None and node13.value == 13

    def test_search_root_and_leaf():
        tree = make_tree()
        root = search(tree, 8)
        assert root is tree and root.value == 8

        leaf = search(tree, 1)
        assert leaf is not None and leaf.value == 1

    def test_search_recursive_no_loops():
        # vérification basique que la fonction est récursive et n'utilise pas de boucle
        src = search.__code__.co_consts  # on n'inspecte pas le code en profondeur, test léger
        assert callable(search)
"""
