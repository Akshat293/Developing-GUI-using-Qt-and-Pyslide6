from PySide6.QtWidgets import QApplication, QMainWindow,QPushButton
from button_holder import ButtonHolder
import sys

# Version 1
"""
app=QApplication(sys.argv)
window=QMainWindow()
window.setWindowTitle("My App")
button=QPushButton("Press me!")
window.setCentralWidget(button)
window.show()
app.exec()
"""

# Version 2
"""
app=QApplication(sys.argv)
class ButtonHolder(QMainWindow):
    def __init__(self,name):  #  parametreized  constructor
        super().__init__() # call the constructor of the parent class
        print(f"Hello {name}")
        self.setWindowTitle("My App")
        button=QPushButton("Press me!")
        self.setCentralWidget(button)  
name='Akshat'
window=ButtonHolder(name) 
window.show()
app.exec()
"""

# Version 3 

app=QApplication(sys.argv) 
window=ButtonHolder("Akshat") 
window.show()
app.exec()

