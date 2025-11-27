# Py_Kata

Ce dépôt contient une collection de **kata Python** inspirés de kata JavaScript.  
Chaque exercice est accompagné de **tests automatisés avec pytest** pour vérifier vos solutions.

---

## Structure du projet
src
    py-kata
        list
        list_advanced
        list_functions
        list_multidimensional
    Tests
        list
        list_advanced
        list_functions
        list_multidimensional

## Instructions pour contribuer

### Forker le projet

1. Cliquez sur le bouton **Fork** en haut à droite du dépôt GitHub.  
2. Clonez votre fork sur votre machine locale :

```bash
git clone https://github.com/<votre-utilisateur>/Py_Kata.git
cd Py_Kata
```

### Créer et activer un environnement virtuel

```bash
python -m venv .venv
source .venv/Scripts/activate
```

**Désaciver la venv**
```bash
deactivate
```

Vous devriez voir (venv) ou (.venv) dans votre terminal après activation.

### Installer les dépendances
```bash
uv sync
```

## Auteur
Projet créé par Tom LEPERT – pour l’apprentissage DataAnalyst et la pratique de Python.