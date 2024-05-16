import datetime as dt

import pytest

from Classes.Classe_Veterinaire import Veterinaire

@pytest.fixture
def setup_vet():
    veterinaire = Veterinaire("JOH123", "Smith", "John",
                      "2004-09-23", [])

    return veterinaire

@pytest.mark.parametrize(
    "date_input, reponse_attendue",
    [
        ("2004-09-23", False),
        (1, False),
        ("Allo", False),
        ("1953-01-05", True)
    ]
)
def test_prendreRetraite(setup_vet, date_input, reponse_attendue):
    vet = setup_vet
    try:
        vet.prendreRetraite()
        assert reponse_attendue
    except (ValueError, TypeError):
        assert not reponse_attendue