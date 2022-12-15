from PySide6.QtWidgets import QWidget,QPushButton,QApplication,QLineEdit,QHBoxLayout,QVBoxLayout,QLabel



class Qline(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.line_edit1=QLineEdit()
        self.line_edit1.setPlaceholderText("Enter your name")
        self.line_edit1.textChanged.connect(self.text_changed)
        self.line_edit1.cursorPositionChanged.connect(self.cursor_position_changed)
        self.line_edit1.editingFinished.connect(self.editing_finished)
        self.line_edit1.selectionChanged.connect(self.selection_changed)



        h_layout=QHBoxLayout()
        label=QLabel("Name:")
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit1)



        v_layout=QVBoxLayout()
        v_layout.addLayout(h_layout)
        button=QPushButton("Enter")
        self.line_edit2=QLabel("Hey")
        v_layout.addWidget(self.line_edit2)
        v_layout.addWidget(button)

        self.setLayout(v_layout)


        

    
       
        self.show()

    def text_changed(self):
        print("Text changed!",self.line_edit1.text())
        self.line_edit2.setText(self.line_edit1.text())

    def cursor_position_changed(self,old,new):
        print(f"Old position: {old}, new position: {new}")

    def editing_finished(self):
        print("Finished editing!")

    def selection_changed(self):
        print("Selection changed!", self.line_edit1.selectedText())


    