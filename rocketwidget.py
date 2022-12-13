from PySide6.QtWidgets import QWidget,QPushButton,QHBoxLayout,QApplication
from PySide6.QtCore import Qt
import sys
class RocketWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        layout=QHBoxLayout()
        button1=QPushButton("Left")
        button2=QPushButton("Center")
        button3=QPushButton("Right")
        button1.setCheckable(True)
        button2.setCheckable(True)
        button3.setCheckable(True)
        button1.clicked.connect(lambda: button1_clicked("Hello",self))
        button2.clicked.connect(lambda: button2_clicked("Hello",self))
        button3.clicked.connect(lambda: button3_clicked("Hello",self))
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        self.setLayout(layout)
        self.show()

def button1_clicked(data,self):
    print("Clicked button1!",data)

def button2_clicked(data,self):
    print("Clicked button2!",data)

def button3_clicked(data,self):
    print("Clicked button3!",data)