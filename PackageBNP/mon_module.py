import sys
import os


def addition(a, b):
    """retourne la somme de a et b

    Args:
        a ([int]): première opérande
        b ([int]): deuxième opérande

    Returns:
        [int]: Somme de a et b

    :Example:
    >>> addition(2,4)
    6
    >>> addition(-2,4)
    2    
    """
    return a + b


def dire_bonjour(name):
    """Salut la personne dont le nom est name

    Args:
        name ([str]): Nom de la personne à saluer

    Returns:
        [str]: Salutation à {name}

    :Example:
    >>> dire_bonjour("Olivier")
    'Bonjour Olivier !'
    """
    return f"Bonjour {name} !"


print(__name__)
if __name__ == "__main__":
    import doctest
    doctest.testmod()  # exécute les exemples comme des tests.
