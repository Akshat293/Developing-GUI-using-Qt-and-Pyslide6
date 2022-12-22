from PySide6.QtWidgets import QWidget,QPushButton,QApplication,QTextEdit,QHBoxLayout,QVBoxLayout

class Qtext(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HTML Editor")
        self.text_edit=QTextEdit()


        current_text_button=QPushButton("Get Current Text")
        current_text_button.clicked.connect(self.get_current_text)

        copy_button=QPushButton("Copy")
        copy_button.clicked.connect(self.text_edit.copy)

        paste_button=QPushButton("Paste")
        paste_button.clicked.connect(self.text_edit.paste) # Go through a custom slot

        cut_button=QPushButton("Cut")
        cut_button.clicked.connect(self.text_edit.cut)

        undo_button=QPushButton("Undo")
        undo_button.clicked.connect(self.text_edit.undo)

        redo_button=QPushButton("Redo")
        redo_button.clicked.connect(self.text_edit.redo)

        set_plain_text_button=QPushButton("Set Plain Text")
        set_plain_text_button.clicked.connect(self.set_plain_text)

        set_html_button=QPushButton("Set HTML")
        set_html_button.clicked.connect(self.set_html)

        clear_button=QPushButton("Clear")
        clear_button.clicked.connect(self.text_edit.clear)

        layout=QHBoxLayout()
        layout.addWidget(current_text_button)
        layout.addWidget(copy_button)
        layout.addWidget(paste_button)
        layout.addWidget(cut_button)
        layout.addWidget(undo_button)
        layout.addWidget(redo_button)
        layout.addWidget(set_plain_text_button)
        layout.addWidget(set_html_button)
        layout.addWidget(clear_button)

        v_layout=QVBoxLayout()
        v_layout.addLayout(layout)
        v_layout.addWidget(self.text_edit)

        self.setLayout(v_layout)



    def paste(self):
        self.text_edit.paste()
        
    def set_plain_text(self):
        self.text_edit.setPlainText("Thankyou for using this app!")

    def set_html(self):
        self.text_edit.setHtml(self.text_edit.toPlainText())

    def get_current_text(self):
        print(self.text_edit.toPlainText())

        

        




