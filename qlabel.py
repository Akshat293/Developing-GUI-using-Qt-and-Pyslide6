from PySide6.QtWidgets import QWidget,QPushButton,QLabel,QVBoxLayout
from PySide6.QtGui import QPixmap

class Qlab(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        qlabel_image= QLabel()
        qlabel_image.setPixmap(QPixmap("images/minion.png"))

        layout=QVBoxLayout()
        layout.addWidget(qlabel_image)
        self.setLayout(layout)





     