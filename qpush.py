from PySide6.QtWidgets import QWidget,QPushButton,QApplication,QHBoxLayout

class Qpush(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button=QPushButton("Press me!")
        button.clicked.connect(self.button_clicked)
        button.pressed.connect(self.button_pressed)
        button.released.connect(self.button_released)
        layout=QHBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)
        self.show()

    def button_clicked(self):
        print("Clicked!")

    def button_pressed(self):
        print("Pressed!")

    def button_released(self):
        print("Released!")

