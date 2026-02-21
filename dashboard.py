from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from theme import DARK_THEME, LIGHT_THEME  # Importer les thèmes

class DashboardWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Style global pour augmenter la taille de la police pour tous les éléments
        self.setStyleSheet(DARK_THEME)
        
        self.setWindowTitle("GenRX - Tableau de bord")
        self.setGeometry(100, 100, 800, 600)
        
        layout = QVBoxLayout()

        # Ajouter du contenu au tableau de bord
        welcome_label = QLabel("Bienvenue dans votre tableau de bord!")
        layout.addWidget(welcome_label)

        self.setLayout(layout)