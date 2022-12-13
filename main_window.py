from PySide6.QtWidgets import QWidget,QPushButton,QHBoxLayout,QApplication,QMainWindow,QToolBar
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon,QAction
import sys

class MainWindow(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.app=app
        self.setWindowTitle("Custom Main Window") # set the title of the window
        # create a menu bar

        menu_bar=self.menuBar()
        menu_bar.setNativeMenuBar(False) # for mac os this is required
        file_menu=menu_bar.addMenu("File")
        quit_action=file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)


        edit_menu=menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")

        menu_bar.addMenu("Window")
        menu_bar.addMenu("Settings")
        menu_bar.addMenu("Help")

        # create a toolbar
        toolbar=QToolBar("My Toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
       
        action1=QAction(QIcon("/Users/akshatsaxena/Desktop/Developing-GUI-using-Qt-and-Pyslide6/images/1.png"),"open",self)
        action1.triggered.connect(self.action1_triggered)
        action1.setStatusTip("This is action 1")
        toolbar.addAction(action1)

    


      



    def quit_app(self):
        print("Quit")
        QApplication.quit()

    def action1_triggered(self):
        print("Action 1 triggered")
   

