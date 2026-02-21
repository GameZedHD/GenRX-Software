from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password_hash = Column(String)
    role = Column(String)

# Exemple d'un modèle simplifié pour les clients
class Client:
    def __init__(self, prenom, nom, telephone, email, adresse, ville, province, code_postal):
        self.prenom = prenom
        self.nom = nom
        self.telephone = telephone
        self.email = email
        self.adresse = adresse
        self.ville = ville
        self.province = province
        self.code_postal = code_postal