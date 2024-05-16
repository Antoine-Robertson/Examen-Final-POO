import pytest

from Classes.Classe_Enclos import Enclos
from Classes.Classe_Animal import Animal

@pytest.fixture
def setup_enclos():
    enclos = Enclos("12345ABC", "Enclos Lions", "Petit",
                      False, "A", [])
    animal = Animal("LI-41524", "Babouche", 15, "Mammifere", "1234ABC", [])

    return enclos, animal

@pytest.mark.parametrize(
    "taille_input, reponse_attendue",
    [
        ("Petit", True),
        (1, False),
        ("Allo", False),
        ("1234", False)
    ]
)
def test_matricule_docteur(setup_enclos, taille_input, reponse_attendue):
    enclos = setup_enclos
    animal = setup_enclos
    enclos.taille = taille_input
    try:
        enclos.estAdapte()
        assert reponse_attendue
    except (ValueError, TypeError):
        assert not reponse_attendue