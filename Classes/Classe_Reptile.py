from Classe_Animal import Animal


class Reptile(Animal):
    """
    Classe Reptile fille de Animal
    """
    def __init__(self, p_numero_animal: str = "", p_surnom: str = "", p_poids: int = 0, p_famille: str = "",
                 p_enclos: str = "", ls_veterinaire: list = None, p_venemeux: bool = None):
        """
        Constructeur de la classe Reptile
        :param p_numero_animal: Animal
        :param p_surnom: Animal
        :param p_poids: Animal
        :param p_famille: Animal
        :param p_venemeux: valeur booleene qui indique si le reptile est venemeux
        """
        super().__init__(p_numero_animal, p_surnom, p_poids, p_famille, p_enclos, ls_veterinaire)

        self._venemeux = p_venemeux

    @property
    def venemeux(self):
        return self._venemeux

    @venemeux.setter
    def venemeux(self, v_venemeux):
        if isinstance(v_venemeux, bool):
            if v_venemeux:
                return f"{self.surnom} est vénémeux"
            else:
                return f"{self.surnom} n'est pas vénémeux"
        else:
            raise TypeError("Type de donnée invalide")
