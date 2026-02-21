import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GenRX - Ajouter un client")

        # Layout principal
        self.layout = QVBoxLayout()

        # Widgets pour ajouter un client
        self.prenom_input = QLineEdit(self)
        self.prenom_input.setPlaceholderText("Prénom")

        self.nom_input = QLineEdit(self)
        self.nom_input.setPlaceholderText("Nom")

        self.telephone_input = QLineEdit(self)
        self.telephone_input.setPlaceholderText("Téléphone")

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Email")

        self.adresse_input = QLineEdit(self)
        self.adresse_input.setPlaceholderText("Adresse")

        self.ville_input = QLineEdit(self)
        self.ville_input.setPlaceholderText("Ville")

        self.province_input = QLineEdit(self)
        self.province_input.setPlaceholderText("Province")

        self.code_postal_input = QLineEdit(self)
        self.code_postal_input.setPlaceholderText("Code Postal")

        # Bouton d'ajout
        self.add_button = QPushButton("Ajouter un client", self)
        self.add_button.clicked.connect(self.add_client)

        # Ajouter les widgets au layout
        self.layout.addWidget(self.prenom_input)
        self.layout.addWidget(self.nom_input)
        self.layout.addWidget(self.telephone_input)
        self.layout.addWidget(self.email_input)
        self.layout.addWidget(self.adresse_input)
        self.layout.addWidget(self.ville_input)
        self.layout.addWidget(self.province_input)
        self.layout.addWidget(self.code_postal_input)
        self.layout.addWidget(self.add_button)

        # Configurer la fenêtre
        self.setLayout(self.layout)
        self.show()

    def add_client(self):
        prenom = self.prenom_input.text()
        nom = self.nom_input.text()
        telephone = self.telephone_input.text()
        email = self.email_input.text()
        adresse = self.adresse_input.text()
        ville = self.ville_input.text()
        province = self.province_input.text()
        code_postal = self.code_postal_input.text()

        # Appel à la fonction d'ajout de client de database.py
        from database import add_client
        add_client(prenom, nom, telephone, email, adresse, ville, province, code_postal)
        print("Client ajouté avec succès!")

# Démarrer l'application
app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())