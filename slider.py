from PySide6.QtWidgets import QApplication, QMainWindow,QPushButton,QSlider
from PySide6.QtCore import Qt
import sys

def response_button_clicked(data):
    print("Clicked!",data)


app=QApplication(sys.argv)
slider=QSlider(Qt.Horizontal)
slider.setMinimum(0)
slider.setMaximum(100)
slider.setValue(50)
slider.valueChanged.connect(response_button_clicked)
slider.show()
app.exec()

