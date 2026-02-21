from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class ClientsPage(QWidget):
    def __init__(self):
        super().__init__()

        # Layout pour cet onglet
        layout = QVBoxLayout()

        # Contenu de la page Clients
        label = QLabel("Gestion des clients.")
        layout.addWidget(label)

        # Définir le layout
        self.setLayout(layout)