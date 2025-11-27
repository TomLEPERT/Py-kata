from typing import List

def build(n: int) -> List[str]:
    """
    Retourne une pyramide de n étages sous forme de liste de chaînes.
    
    Exemples:
    build(5) -> [
        "    *    ",
        "   ***   ",
        "  *****  ",
        " ******* ",
        "*********"
    ]
    
    Si n <= 0, lève RangeError.
    Si n n'est pas un entier, lève TypeError.
    
    Ton code en dessous
    """



"""
Lancer le test : 
Dans le terminal se positioner dans le dossier src
Utiliser la commande : pytest tests/list_advanced/test_pyramid.py -q

Aperçu du test : 

def test_basic_pyramid():
    assert build(1) == ["*"]
    assert build(2) == [" * ", "***"]
    assert build(5) == [
        "    *    ",
        "   ***   ",
        "  *****  ",
        " ******* ",
        "*********",
    ]

def test_invalid_values():
    import builtins
    with pytest.raises(ValueError):
        build(0)
    with pytest.raises(ValueError):
        build(-1)
    with pytest.raises(TypeError):
        build(None)
    with pytest.raises(TypeError):
        build("a")
"""