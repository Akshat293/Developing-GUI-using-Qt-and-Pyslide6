from PySide6.QtWidgets import QApplication, QMainWindow,QPushButton

def button_clicked(data):
    print("Clicked!",data)
class ButtonHolder(QMainWindow):
    def __init__(self,name):  #  parametreized  constructor
        super().__init__() # call the constructor of the parent class
        print(f"Hello {name}")
        self.setWindowTitle("My App")
        button1=QPushButton("Press me!")
        button1.setCheckable(True) # make the button checkable
        button1.clicked.connect(button_clicked) # connect the signal to the slot
        self.setCentralWidget(button1)