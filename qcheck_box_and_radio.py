from PySide6.QtWidgets import QWidget,QPushButton,QLabel,QVBoxLayout,QLineEdit,QSizePolicy,QHBoxLayout,QGridLayout,QCheckBox,QRadioButton,QApplication,QGroupBox

class Qchk(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCheckBox and QRadioButton")

        os=QGroupBox("Operating System:")
        windows=QCheckBox("Windows")
        windows.toggled.connect(self.windows_toggled)
        linux=QCheckBox("Linux")
        linux.toggled.connect(self.linux_toggled)
        mac=QCheckBox("Mac")
        mac.toggled.connect(self.mac_toggled)

        os_layout=QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)
        os.setLayout(os_layout)

        answers=QGroupBox("Choose your answers:")
        answer_1=QRadioButton("Answer 1")
        answer_1.clicked.connect(self.answer_1_clicked)
        answer_2=QRadioButton("Answer 2")

        answer_3=QRadioButton("Answer 3")
        answer_4=QRadioButton("Answer 4")

        answers_layout=QVBoxLayout()
        answers_layout.addWidget(answer_1)
        answers_layout.addWidget(answer_2)
        answers_layout.addWidget(answer_3)
        answers_layout.addWidget(answer_4)

        answers.setLayout(answers_layout)

        layout=QVBoxLayout()
        layout.addWidget(os)
        layout.addWidget(answers)
        self.setLayout(layout)

    def windows_toggled(self,checked):
        if checked :
            print("Windows is checked")
        else:
            print("Windows is unchecked")
    
    def linux_toggled(self,checked):
        if checked :
            print("Linux is checked")
        else:
            print("Linux is unchecked")

    def mac_toggled(self,checked):
        if checked :
            print("Mac is checked")
        else:
            print("Mac is unchecked")

    def answer_1_clicked(self,checked):
        if checked :
            print("Answer 1 is checked")
        else:
            print("Answer 1 is unchecked")

      




       