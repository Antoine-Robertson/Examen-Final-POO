# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.Dialog_animal
from PyQt5 import QtWidgets

from Classes.Classe_Animal import Animal
from Classes.Classe_Reptile import Reptile
from Classes.Classe_Oiseau import Oiseau
from Classes.Classe_Mammifere import Mammifere

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetreanimal(QtWidgets.QDialog, UI_PY.Dialog_animal.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetreanimal, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue animal")

    @pyqtSlot()
    def on_pushButton_ajouter_clicked(self):
        num_animal = self.lineEdit_numero_animal.text()
        surnom = self.lineEdit_surnom_animal.text()
        poids = self.lineEdit_poids_animal.text()
        famille = self.comboBox_famille_animal.objectName()
        enclos = self.comboBox_enclos_animal.objectName()
        if self.comboBox_famille_animal.objectName() == "Mammifères":
            couleur = self.comboBox_couleur_poil.objectName()
            mammifere = Mammifere(f"{num_animal}", f"{surnom}", poids, f"{famille}",
                                  f"{enclos}", [], f"{couleur}")
            mammifere.serialiserAnimal()
        if self.comboBox_famille_animal.objectName() == "Oiseaux":
            if self.lineEdit_longueur_bec.text().isnumeric():
                longueur = float(self.lineEdit_longueur_bec.text())
            oiseau = Oiseau(f"{num_animal}", f"{surnom}", poids, f"{famille}",
                                  f"{enclos}", [], longueur)
            oiseau.serialiserAnimal()
        if self.comboBox_famille_animal.objectName() == "Réptiles":
            if self.comboBox_venimeux.objectName() == "True":
                venimeux = True
            else:
                venimeux = False
            reptile = Reptile(f"{num_animal}", f"{surnom}", poids, f"{famille}",
                                  f"{enclos}", [], venimeux)
            reptile.serialiserAnimal()