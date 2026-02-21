from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QTabWidget
from PyQt5.QtGui import QPixmap, QIcon
from clients import ClientsPage  # Importer la page Clients
from employees import EmployeesPage  # Importer la page Employés
from documents import DocumentsPage  # Importer la page Documents
from PyQt5.QtCore import Qt
from theme import DARK_THEME, LIGHT_THEME  # Importer les thèmes

class DashboardWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Style global pour augmenter la taille de la police pour tous les éléments
        self.setStyleSheet(DARK_THEME)

        # Configuration de la fenêtre principale
        self.setWindowTitle("GenRX - Tableau de bord")
        self.setGeometry(100, 100, 800, 600)

        # Layout principal
        layout = QVBoxLayout()

        # Afficher le logo GenRX
        logo = QLabel(self)
        pixmap = QPixmap("static/images/GenRXlogo.png")
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignCenter)  # Centrer le logo
        layout.addWidget(logo)

        # Création du widget des onglets
        self.tabs = QTabWidget()

        # Onglets avec icônes
        self.tabs.addTab(ClientsPage(), QIcon("static/icons/clients.png"), "Clients")
        self.tabs.addTab(EmployeesPage(), QIcon("static/icons/employees.png"), "Employés")
        self.tabs.addTab(DocumentsPage(), QIcon("static/icons/documents.png"), "Documents")

        # Ajouter les onglets au layout principal
        layout.addWidget(self.tabs)

        # Appliquer le layout à la fenêtre
        self.setLayout(layout)