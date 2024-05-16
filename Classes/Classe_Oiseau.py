from Classe_Animal import Animal


class Oiseau(Animal):
    """
    Classe Oiseau fille de Animal
    """
    def __init__(self, p_numero_animal: str = "", p_surnom: str = "", p_poids: int = 0, p_famille: str = "",
                 p_enclos: str = "", ls_veterinaire: list = None, p_longueur_bec: float = 0.0):
        """
        Constructeur de la classe Oiseau
        :param p_numero_animal: Animal
        :param p_surnom: Animal
        :param p_poids: Animal
        :param p_famille: Animal
        :param p_longueur_bec: Longueur du bec de l'oiseau en nombre réel positif
        """
        super().__init__(p_numero_animal, p_surnom, p_poids, p_famille, p_enclos, ls_veterinaire)

        self._longueur_bec = p_longueur_bec

    @property
    def longueur_bec(self):
        return self._longueur_bec

    @longueur_bec.setter
    def longueur_bec(self, v_longuer_bec):
        if isinstance(v_longuer_bec, float) and v_longuer_bec > 0.0:
            self._longueur_bec = v_longuer_bec
        else:
            raise ValueError("Longueur de bec invalide")