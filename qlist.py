from PySide6.QtWidgets import QWidget,QPushButton,QLabel,QVBoxLayout,QLineEdit,QSizePolicy,QHBoxLayout,QGridLayout,QCheckBox,QRadioButton,QApplication,QGroupBox,QListWidget,QComboBox

class Qlist(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListWidget and QComboBox")
        self.resize(500,500)

        self.list_widget=QListWidget()
        self.list_widget.setSelectionMode(QListWidget.MultiSelection)
        self.list_widget.addItems(["Item 1","Item 2","Item 3","Item 4","Item 5"])
        self.list_widget.currentItemChanged.connect(self.list_item_changed)
        self.list_widget.currentTextChanged.connect(self.list_text_changed)

        button_add=QPushButton("Add Item")
        button_add.clicked.connect(self.add_item)

        button_remove=QPushButton("Remove Item")
        button_remove.clicked.connect(self.remove_item)

        button_clear=QPushButton("Clear List")
        button_clear.clicked.connect(self.clear_list)

        button_item_count=QPushButton("Item Count")
        button_item_count.clicked.connect(self.item_count)

        button_selected_item=QPushButton("Selected Item")
        button_selected_item.clicked.connect(self.selected_item)


        h_layout=QHBoxLayout()
        h_layout.addWidget(button_add)
        h_layout.addWidget(button_remove)
        h_layout.addWidget(button_clear)
        h_layout.addWidget(button_item_count)
        h_layout.addWidget(button_selected_item)

      

   
        v_layout=QVBoxLayout()
        v_layout.addWidget(self.list_widget)
        v_layout.addLayout(h_layout)
        self.setLayout(v_layout)



    def list_item_changed(self,current_item,previous_item):
        print("Current item is: "+current_item.text())
        print("Previous item is: "+previous_item.text())

    def list_text_changed(self,current_text):
        print("Current text is: "+current_text)

    def add_item(self):
        self.list_widget.addItem(f"Item {self.list_widget.count()+1}")

    def remove_item(self):
        self.list_widget.takeItem(self.list_widget.currentRow())

    def clear_list(self):
        self.list_widget.clear()

    def item_count(self):
        print("Item count is: "+str(self.list_widget.count()))

    def selected_item(self):
        list=self.list_widget.selectedItems()
        for item in list:
            print("Selected item is: "+item.text())




        