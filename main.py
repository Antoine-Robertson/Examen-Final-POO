####################################################################################
###  420-2G4 - Programmation orientée objet
###  Travail: Exercice  gestion du zoo
###  Nom: Antoine Robertson
###  No étudiant: 2191070
###  No Groupe: 1
###  Description du fichier: Programme principal
####################################################################################

#######################################
###  IMPORTATIONS - Portée globale  ###
########+###############################

# Importer le module sys nécessaire à l'exécution.
import sys
import PyQt5
from PyQt5 import QtWidgets

#importer les interfaces graphiques
import UI_PY.MainWindow_zoo
from PyQt5.QtCore import pyqtSlot
# Pour la réinitialisation de la date dans le dateEdit
from PyQt5.QtCore import QDate
# Importer Pour le model de la listView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from Dialog.dialog_animal import Fenetreanimal
from Dialog.dialog_recherche import Fenetrerecherche
from Dialog.dialog_veterinaire import Fenetreveterinaire

from Classes.Classe_Enclos import Enclos

#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

########################################################
###### DÉFINITIONS DE LA CLASSE fenetrePrincipale ######
########################################################
# Créer une classe qui hérite de Qt et de notre ui.
# Nom de ma classe (fenetrePrincipal)

enclos1 = Enclos("12345ABC", "Enclos des Lions", "Petit", False,
                 "A", [])

enclos2 = Enclos("54321CBA", "Enclos des Moutons", "Grand", False,
                 "B", [])

print(Enclos.ls_enclos)
print(enclos2.numero_enclos)

class fenetrePrincipale(QtWidgets.QMainWindow, UI_PY.MainWindow_zoo.Ui_MainWindow):
    """
    Nome de la classe : fenetrePrincipale
    Héritages :
    - QtWidgets.QMainWindow : Type d'interface créé par QtDesigner
    - interfacegraphique.Ui_MainWindow_pharmacie : Ma classe générée avec QtDesigner
    """
    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QMainWindow et MainWindow_pharmacie.Ui_MainWindow
        """
        # Appeler le constructeur parent avec ma classe en paramètre...
        super(fenetrePrincipale, self).__init__(parent)
        # Préparer l'interface utilisateur
        self.setupUi(self)
        # Donner un titre à la fenêtre principale
        self.setWindowTitle("Gestion du zoo")

    # gastionnaire d'événement du bouton Animal
    @pyqtSlot()
    def on_pushButton_animal_clicked(self):
        # Instancier une boite de dialogue FenetreListview
        dialog = Fenetreanimal()
        # Afficher la boite de dialogue
        dialog.show()
        dialog.exec_()

    @pyqtSlot()
    def on_pushButton_recherche_clicked(self):
        # Instancier une boite de dialogue FenetreListview
        dialog = Fenetrerecherche()
        # Afficher la boite de dialogue
        #dialog.show()
        #dialog.exec_()

    @pyqtSlot()
    def on_pushButton_veterinaire_clicked(self):
        # Instancier une boite de dialogue FenetreListview
        dialog = Fenetreveterinaire()
        # Afficher la boite de dialogue
        #dialog.show()
        #dialog.exec_()
#################################
###### PROGRAMME PRINCIPAL ######
#################################
# Créer le main qui lance la fenêtre de Qt
def main():
    """
    Méthode main : point d'entré du programme.
    Exécution de l'applicatin avec l'interface graphique.
    reply = Dialog.exec_()
    """
    # Instancier une application et une fenetre principale
    app = QtWidgets.QApplication(sys.argv)
    form = fenetrePrincipale()
    # Afficher la fenêtre principale
    form.show()
    # Lancer l'application
    app.exec()

if __name__ == "__main__":
    main()