import os
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication
from setup import SetupWindow  # Assurez-vous d'importer SetupWindow si ce n'est pas déjà fait
from login import LoginWindow  # Assurez-vous d'importer LoginWindow si ce n'est pas déjà fait

# Définir le chemin dynamique
if getattr(sys, 'frozen', False):  # Si l'application est en mode exécutable
    base_path = sys._MEIPASS  # Répertoire temporaire pour PyInstaller
else:
    base_path = os.path.dirname(__file__)  # Répertoire de travail normal

# Spécifie le chemin de la base de données
db_path = os.path.join(base_path, 'genrx_database.db')

# Fonction pour se connecter à la base de données
def connect_db():
    conn = sqlite3.connect(db_path)  # Utiliser le chemin dynamique pour la base
    return conn

# Fonction pour vérifier si un utilisateur existe dans la base de données
def check_if_user_exists():
    conn = connect_db()  # Se connecter à la base de données
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users LIMIT 1")  # Vérifier si au moins un utilisateur existe
    user = cursor.fetchone()
    conn.close()
    return user is not None

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Vérifier si un utilisateur existe déjà dans la base de données
    if check_if_user_exists():  # Si un utilisateur existe, ouvrir la page de connexion
        window = LoginWindow()
    else:  # Si aucun utilisateur n'existe, ouvrir la page de configuration
        window = SetupWindow()

    window.show()
    sys.exit(app.exec_())