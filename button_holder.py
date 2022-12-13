from PySide6.QtWidgets import QApplication, QMainWindow,QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self,name):  #  parametreized  constructor
        super().__init__() # call the constructor of the parent class
        print(f"Hello {name}")
        self.setWindowTitle("My App")
        button=QPushButton("Press me!")
        self.setCentralWidget(button)  