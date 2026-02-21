import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sqlite3  # Pour SQLite
import bcrypt  # Importer bcrypt pour vérifier les mots de passe
from theme import DARK_THEME, LIGHT_THEME  # Importer les thèmes

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GenRX Database - Connexion")
        self.setGeometry(100, 100, 400, 250)
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

        # Formulaire de connexion
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Nom d'utilisateur")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Mot de passe")

        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)

        # Bouton pour se connecter
        self.login_button = QPushButton("Se connecter")
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def verify_password(self, entered_password, stored_hash):
        # Comparer le mot de passe entré avec le mot de passe haché
        return bcrypt.checkpw(entered_password.encode('utf-8'), stored_hash.encode('utf-8'))

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Vérification des informations d'identification
        conn = sqlite3.connect("genrx_database.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and self.verify_password(password, user[2]):  # user[2] est le password_hash
            self.show_success("Connexion réussie!")
            self.close()  # Ferme la fenêtre de connexion
            # Tu peux maintenant rediriger vers le dashboard ou une autre page principale
        else:
            self.show_error("Nom d'utilisateur ou mot de passe incorrect!")

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
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())