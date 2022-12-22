from PySide6.QtWidgets import QWidget,QPushButton,QLabel,QVBoxLayout,QLineEdit,QSizePolicy,QHBoxLayout,QGridLayout,QCheckBox,QRadioButton,QComboBox,QGroupBox


class Qcombo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox")
        combo_box=QComboBox(self)
        combo_box.addItem("Item 1")
        combo_box.addItem("Item 2")
        combo_box.addItem("Item 3")

        combo_box.currentIndexChanged.connect(self.combo_box_changed)
        combo_box.currentTextChanged.connect(self.combo_box_changed_text)

        



    def combo_box_changed(self,index):
        print("Current index is: "+str(index))

    def combo_box_changed_text(self,text):
        print("Current text is: "+text)

        

