from Classe_Enclos import Enclos
from Classe_Veterinaire import Veterinaire
import jsonpickle

class Animal:

    ls_familles = ["Mammifere", "Oiseau", "Reptile"]
    nb_animaux = 0
    ls_animaux = []

    def __init__(self, p_numero_animal: str = "", p_surnom: str = "", p_poids: int = 0, p_famille: str = "",
                 p_enclos: str = "", ls_veterinaire: list = None):
        """
        Constructeur de la classe Animal
        :param p_numero_animal: 2 lettres suivies d'un tiret puis 5 chiffres
        :param p_surnom: surnom de l'Animal
        :param p_poids: nombre entier supérieur à 15 lbs
        :param p_famille: soit mammifere, oiseau ou reptile
        """
        self._numero_animal = p_numero_animal
        self._surnom = p_surnom
        self._poids = p_poids
        self._famille = p_famille
        self._enclos = p_enclos
        self.ls_veterinaire = ls_veterinaire
        Animal.ls_animaux.append(self)
        Animal.nb_animaux += 1

    @property
    def numero_animal(self):
        return self._numero_animal

    @numero_animal.setter
    def numero_animal(self, v_numero_animal):
        if (isinstance(v_numero_animal, str) and len(v_numero_animal) == 8 and v_numero_animal[:1].isalpha() and
                v_numero_animal[2] == "-" and v_numero_animal[-5:].isnumeric()):
            self._numero_animal = v_numero_animal
        else:
            raise ValueError("Numéro de l'animal invalide")

    @property
    def surnom(self):
        return self._surnom

    @surnom.setter
    def surnom(self, v_surnom):
        self._surnom = v_surnom

    @property
    def poids(self):
        return self._poids

    @poids.setter
    def poids(self, v_poids):
        if isinstance(v_poids, int) and v_poids >= 15:
            self._poids = v_poids

    @property
    def enclos(self):
        return self._enclos

    @enclos.setter
    def enclos(self, v_enclos):
        if isinstance(v_enclos, str):
            for e in Enclos.ls_enclos:
                if e.numero_enclos == v_enclos:
                    self._enclos = v_enclos
                else:
                    raise ValueError("Enclos inexistant")
        else:
            raise ValueError("Numéro d'enclos invalide")

    def ajouterEnclosVeterinaire(self, veterinaire, enclos):
        for v in self.ls_veterinaire:
            if v == veterinaire:
                for e in Enclos.ls_enclos:
                    if e.numero_enclos == enclos:
                        veterinaire.list_enclos.append(e)
                    else:
                        raise ValueError("Enclos inexistant")
            else:
                raise ValueError("Vétérinaire inexistant")

    def serialiserAnimal(self):
        with open(f"{self.numero_animal}", "w") as F:
            F.write(jsonpickle.encode(self))

    def __str__(self):
        return (f"Numéro: {self.numero_animal}\n"
                f"Surnom: {self.surnom}\n"
                f"Poids: {self.poids}\n"
                f"Famille: {self._famille}\n"
                f"Enclos: {self._enclos}\n"
                f"Vétériniares: {self.ls_veterinaire}\n")