class Enclos:

    ls_enclos = []
    nb_enclos = 0
    dict_taille = {"Petit": 2, "Moyen": 4, "Grand": 6}
    ls_sections = ["A", "B", "C"]

    def __init__(self, p_numero_enclos: str = "", p_nom_enclos: str = "", p_taille: str = "", p_type: bool = None,
                 p_localisation: str = "", ls_animaux_enclos: list = None):
        """
        Constructeurr de la classe Enclos
        :param numero_enclos:
        :param nom_enclos:
        :param taille:
        :param type:
        :param localisation:
        :param ls_animaux_enclos:
        """
        self._numero_enclos = p_numero_enclos
        self._nom_enclos = p_nom_enclos
        self._taille = p_taille
        self._type = p_type
        self._localisation = p_localisation
        self.ls_animaux_enclos = ls_animaux_enclos
        Enclos.ls_enclos.append(self)
        Enclos.nb_enclos += 1

    @property
    def numero_enclos(self):
        return self._numero_enclos

    @numero_enclos.setter
    def numero_enclos(self, v_numero_enclos):
        if isinstance(v_numero_enclos, str) and v_numero_enclos[:4].isnumeric() and v_numero_enclos[-3:].isalpha():
            self._numero_enclos = int(v_numero_enclos)
        else:
            raise ValueError("Numero d'enclos invalide")

    @property
    def nom_enclos(self):
        return self._nom_enclos

    @nom_enclos.setter
    def nom_enclos(self, v_nom_enclos):
        if isinstance(v_nom_enclos, str) and len(v_nom_enclos) <= 25:
            self._nom_enclos = v_nom_enclos
        else:
            raise ValueError("Nom d'enclos invalide")

    @property
    def taille(self):
        return self._taille

    @taille.setter
    def taille(self, v_taille):
        if isinstance(v_taille, str):
            for t in Enclos.dict_taille.keys():
                if t == v_taille.capitalize():
                    self._taille = t
                else:
                    raise ValueError("Taille invalide")
        else:
            raise ValueError("Taille invalide")

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, v_type):
        if v_type.capitalize() == "Intérieur":
            return True
        elif v_type.capitalize() == "Extérieur":
            return False

    @property
    def localisation(self):
        return self._localisation

    @localisation.setter
    def localisation(self, v_localisation):
        if isinstance(v_localisation, str):
            for s in Enclos.ls_sections:
                if s == v_localisation.capitalize():
                    self._localisation = s
                else:
                    raise ValueError("Section invalide")
        else:
            raise ValueError("Localisation invalide")

    def estAdapte(self):
        for t in Enclos.dict_taille.keys():
            if self.taille.capitalize() == t:
                if Enclos.dict_taille[t] <= len(self.ls_animaux_enclos):
                    return True
                else:
                    return False
            else:
                raise ValueError("Taille invalide")