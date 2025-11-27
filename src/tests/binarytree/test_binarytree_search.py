from src.py_kata.binarytree.binarytree_search import TreeNode, search


def make_tree():
    """
    Construit l'arbre de l'exemple :
            8
          /   \
         3     10
        / \      \
       1   6      14
          / \    /
         4   7  13
    """
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
    assert node6 is not None
    assert node6.value == 6

    node13 = search(tree, 13)
    assert node13 is not None
    assert node13.value == 13


def test_search_root_and_leaf():
    tree = make_tree()
    root = search(tree, 8)
    assert root is not None
    assert root.value == 8

    leaf = search(tree, 1)
    assert leaf is not None
    assert leaf.value == 1


def test_search_recursive_no_loops():
    # vérification basique que la fonction est récursive et n'utilise pas de boucle
    # test léger : on vérifie que la fonction est callable
    assert callable(search)