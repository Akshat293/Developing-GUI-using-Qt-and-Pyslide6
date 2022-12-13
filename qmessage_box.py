from PySide6.QtWidgets import QWidget,QPushButton,QHBoxLayout,QApplication,QMessageBox
from PySide6.QtCore import Qt
import sys

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QMessageBox')

        button_hard=QPushButton('Hard')
        button_hard.clicked.connect(self.button_clicked_hard)

        button_critical=QPushButton('Medium')
        button_critical.clicked.connect(self.button_clicked_critical)

        button_question=QPushButton('Question')
        button_question.clicked.connect(self.button_clicked_question)

        button_information=QPushButton('Information')
        button_information.clicked.connect(self.button_clicked_information)

        button_warning=QPushButton('Warning')
        button_warning.clicked.connect(self.button_clicked_warning)

        button_about=QPushButton('About')
        button_about.clicked.connect(self.button_clicked_about)


        # Set up the layout
        layout=QHBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)
        self.setLayout(layout)



    def button_clicked_hard(self):
        messages=QMessageBox()
        messages.setMinimumSize(500,500)
        messages.setWindowTitle('Hard')
        messages.setText('This is a hard message')
        messages.setIcon(QMessageBox.Warning)
        messages.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        messages.setDefaultButton(QMessageBox.Ok)
        ret=messages.exec()
        if ret==QMessageBox.Ok:
            print('Ok')
        else:
            print('Cancel')



    def button_clicked_critical(self):
        messages=QMessageBox()
        messages.setMinimumSize(500,500)
        messages.setWindowTitle('Critical')
        messages.setText('This is a critical message')
        messages.setIcon(QMessageBox.Critical)
        messages.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        messages.setDefaultButton(QMessageBox.Ok)
        ret=messages.exec()
        if ret==QMessageBox.Ok:
            print('Ok')
        else:
            print('Cancel')


    def button_clicked_question(self):
        messages=QMessageBox()
        messages.setMinimumSize(500,500)
        messages.setWindowTitle('Question')
        messages.setText('This is a question message')
        messages.setIcon(QMessageBox.Question)
        messages.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        messages.setDefaultButton(QMessageBox.Ok)
        ret=messages.exec()
        if ret==QMessageBox.Ok:
            print('Ok')
        else:
            print('Cancel')

    def button_clicked_information(self):
        messages=QMessageBox()
        messages.setMinimumSize(500,500)
        messages.setWindowTitle('Information')
        messages.setText('This is a information message')
        messages.setIcon(QMessageBox.Information)
        messages.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        messages.setDefaultButton(QMessageBox.Ok)
        ret=messages.exec()
        if ret==QMessageBox.Ok:
            print('Ok')
        else:
            print('Cancel')

    def button_clicked_warning(self):
        messages=QMessageBox()
        messages.setMinimumSize(500,500)
        messages.setWindowTitle('Warning')
        messages.setText('This is a warning message')
        messages.setIcon(QMessageBox.Warning)
        messages.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        messages.setDefaultButton(QMessageBox.Ok)
        ret=messages.exec()
        if ret==QMessageBox.Ok:
            print('Ok')
        else:
            print('Cancel')

    def button_clicked_about(self):
        ret=QMessageBox.about(self,'About','This is a about message')
        if ret==QMessageBox.Ok:
            print('Ok')
        else:
            print('Cancel')







      