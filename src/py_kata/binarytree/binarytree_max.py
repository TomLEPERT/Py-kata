from typing import Optional

"""
En informatique, un arbre binaire est une structure de données arborescente
dans laquelle chaque nœud a au maximum deux enfants : un enfant gauche et un enfant droit.

On vous fournit un arbre binaire. Implémentez la fonction `max_value` qui
retourne la valeur maximale présente dans l'arbre.

Exemple d'arbre :

        7
      /   \
     5     2
      \      \
       6      11
      / \    /
     1   9  4

Résultat attendu : 11

Si le nœud racine est None, la fonction doit retourner None.

Cette fonction doit être récursive : vous ne pouvez pas utiliser de boucle.
"""

class TreeNode:
    def __init__(self, value, left=None, right=None):
        """
        Initialisation d'un nœud d'arbre binaire.
        
        value : valeur du nœud (entier)
        left : nœud enfant gauche (ou None)
        right : nœud enfant droit (ou None)
        """
        self.value = value
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right

def max_value(node: Optional[TreeNode]) -> Optional[int]:
    """
    Retourne la valeur maximale dans un arbre binaire.

    - Si le nœud est None, retourne None.
    - Doit être récursive : aucune boucle n'est autorisée.
    
    Ton code en dessous
    """





"""
Lancer le test : 
Dans le terminal se positioner dans le dossier src
Utiliser la commande : pytest tests/binarytree/test_binarytree_max.py -q

Aperçu du test : 

def test_max_value_basic():
    # Arbre vide
    assert max_value(None) is None

    # Arbre avec un seul nœud
    assert max_value(TreeNode(42)) == 42

    # Exemple complet
    tree = TreeNode(
        7,
        TreeNode(
            5,
            None,
            TreeNode(6, TreeNode(1), TreeNode(9))
        ),
        TreeNode(
            2,
            None,
            TreeNode(11, TreeNode(4), None)
        )
    )
    assert max_value(tree) == 11

def test_max_value_variants():
    # Arbre avec plusieurs niveaux
    tree = TreeNode(
        10,
        TreeNode(20, TreeNode(5), TreeNode(15)),
        TreeNode(30, None, TreeNode(25))
    )
    assert max_value(tree) == 30

    # Arbre avec nœud unique 0
    tree = TreeNode(0)
    assert max_value(tree) == 0
"""