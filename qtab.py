from PySide6.QtWidgets import QWidget,QPushButton,QLabel,QVBoxLayout,QLineEdit,QSizePolicy,QHBoxLayout,QGridLayout,QCheckBox,QRadioButton,QApplication,QGroupBox,QListWidget,QComboBox,QTableWidget,QTableWidgetItem,QTabWidget

class Qtab(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget")
        self.resize(500,500)
        tab_widget=QTabWidget(self)

        # Information Tab
        widget_form=QWidget()
        label_full_name=QLabel("Name")
        form_layout=QHBoxLayout()
        form_layout.addWidget(label_full_name)
        form_layout.addWidget(QLineEdit())
        widget_form.setLayout(form_layout)

        # Education Tab
        widget_education=QWidget()
        label_education=QLabel("Education")
        education_layout=QHBoxLayout()
        education_layout.addWidget(label_education)
        education_layout.addWidget(QLineEdit())
        widget_education.setLayout(education_layout)


        tab_widget.addTab(widget_form,"Information")
        tab_widget.addTab(widget_education,"Education")

        layout=QVBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)

        



       

       

