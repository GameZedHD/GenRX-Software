import os
import sys
import sqlite3

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