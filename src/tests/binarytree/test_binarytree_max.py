from src.py_kata.binarytree.binarytree_max import TreeNode, max_value

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