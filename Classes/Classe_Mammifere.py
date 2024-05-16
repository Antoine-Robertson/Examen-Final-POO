from Classe_Animal import Animal


class Mammifere(Animal):
    """
    Classe Mammifere, fille de Animal
    """

    ls_couleur = ["Noir", "Blanc", "Brun", "Gris", "Beige", "Mutli"]

    def __init__(self, p_numero_animal: str = "", p_surnom: str = "", p_poids: int = 0, p_famille: str = "",
                 p_enclos: str = "", ls_veterinaire: list = None, p_couleur_poil: str = ""):
        """
        Constructeur de la classe Mammifere
        :param p_numero_animal: Animal
        :param p_surnom: Animal
        :param p_poids: Animal
        :param p_famille: Animal
        :param p_couleur_poil: Couleur du poil du Mammifere selon un liste de couleurs possibles
        """
        Animal.__init__(self, p_numero_animal, p_surnom, p_poids, p_famille, p_enclos, ls_veterinaire)
        self._couleur_poil = p_couleur_poil

    @property
    def couleur_poil(self):
        return self._couleur_poil

    @couleur_poil.setter
    def couleur_poil(self, v_couleur_poil):
        if isinstance(v_couleur_poil, str):
            for c in Mammifere.ls_couleurs:
                if c == v_couleur_poil.capitalize():
                    self._couleur_poil = v_couleur_poil
                else:
                    raise ValueError("Couleur invalide")
        else:
            raise ValueError("type de donnée invalide")

    def __str__(self):
        return (f"Numéro: {self.numero_animal}\n"
                f"Surnom: {self.surnom}\n"
                f"Poids: {self.p_poids} lbs\n"
                f"Famille: {self.p_famille}\n"
                f"Couleur du poil: {self.couleur_poil}\n")