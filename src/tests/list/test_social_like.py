from src.py_kata.list.social_like import social_like

def test_social_like_various():
    assert social_like([]) == "no one likes this"
    assert social_like(["Peter"]) == "Peter likes this"
    assert social_like(["Jacob","Alex"]) == "Jacob and Alex like this"
    assert social_like(["Max","John","Mark"]) == "Max, John and Mark like this"
    assert social_like(["Alex","Jacob","Mark","Max"]) == "Alex, Jacob and 2 others like this"
    assert social_like(["A","B","C","D","E"]) == "A, B and 3 others like this"