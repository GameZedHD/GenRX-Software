import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import bcrypt
import sqlite3  # Pour SQLite
import subprocess  # Importer subprocess pour ouvrir login.py après setup
from theme import DARK_THEME, LIGHT_THEME  # Importer les thèmes
from auth import hash_password  # Importer la fonction de hachage

class SetupWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Appliquer le thème sombre
        self.setStyleSheet(DARK_THEME)

        self.setWindowTitle("GenRX Database - Configuration")
        self.setGeometry(100, 100, 400, 300)
        self.setFixedSize(550, 350)  # Remplace les dimensions par ce que tu veux

        layout = QVBoxLayout()

        # Style global pour augmenter la taille de la police pour tous les éléments
        self.setStyleSheet(DARK_THEME)

        # Logo
        self.logo = QLabel(self)
        pixmap = QPixmap("D:\GenRX\static\images\GenRXlogo.png")  # Remplace par le chemin de ton logo
        self.logo.setPixmap(pixmap)
        self.logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.logo)

        # Formulaire de création de compte
        form_layout = QFormLayout()
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Nom d'utilisateur")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Mot de passe")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password2_input = QLineEdit()
        self.password2_input.setPlaceholderText("Confirmer le mot de passe")
        
        form_layout.addRow("Nom d'utilisateur:", self.username_input)
        form_layout.addRow("Mot de passe:", self.password_input)
        form_layout.addRow("Confirmer le mot de passe:", self.password2_input)

        layout.addLayout(form_layout)

        # Bouton pour créer le compte
        self.create_button = QPushButton("Créer le compte administrateur")
        self.create_button.setStyleSheet("font-weight: bold;")
        self.create_button.clicked.connect(self.create_account)
        layout.addWidget(self.create_button)

        self.setLayout(layout)

    def create_account(self):
        username = self.username_input.text()
        password = self.password_input.text()
        password2 = self.password2_input.text()

        # Vérification des champs
        if username == "" or password == "" or password2 == "":
            self.show_error("Tous les champs doivent être remplis.")
            return

        if password != password2:
            self.show_error("Les mots de passe ne correspondent pas.")
            return

        # Hacher le mot de passe avant de l'enregistrer
        password_hashed = hash_password(password)

        # Créer la base de données et la table si elles n'existent pas
        conn = sqlite3.connect("genrx_database.db")
        cursor = conn.cursor()

        # Création de la table users si elle n'existe pas
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        ''')

        # Vérification si le nom d'utilisateur existe déjà
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        if cursor.fetchone():
            self.show_error("Nom d'utilisateur déjà pris.")
            conn.close()
            return

        # Création du compte administrateur avec le mot de passe haché
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hashed))
        conn.commit()
        conn.close()

        self.show_success("Compte administrateur créé avec succès!")

        # Ouvrir le fichier login.py après création du compte
        subprocess.run(["python", "login.py"])  # Cela ouvrira login.py directement

        self.close()  # Fermer la fenêtre setup après avoir créé le compte

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Erreur")
        msg.exec_()

    def show_success(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Succès")
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SetupWindow()
    window.show()
    sys.exit(app.exec_())