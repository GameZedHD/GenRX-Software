import sqlite3

# Créer une connexion à la base de données SQLite
def connect_db():
    conn = sqlite3.connect('genrx_database.db')  # Crée le fichier si il n'existe pas
    return conn

# Créer la table des clients
def create_table():
    conn = connect_db()
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        prenom TEXT NOT NULL,
        nom TEXT NOT NULL,
        telephone TEXT,
        email TEXT,
        adresse TEXT,
        ville TEXT,
        province TEXT,
        code_postal TEXT
    )''')

    conn.commit()
    conn.close()

# Pour ajouter un client dans la base
def add_client(prenom, nom, telephone, email, adresse, ville, province, code_postal):
    conn = connect_db()
    c = conn.cursor()

    c.execute('''INSERT INTO clients (prenom, nom, telephone, email, adresse, ville, province, code_postal)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
              (prenom, nom, telephone, email, adresse, ville, province, code_postal))

    conn.commit()
    conn.close()