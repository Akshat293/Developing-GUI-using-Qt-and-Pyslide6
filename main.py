from PySide6.QtWidgets import QApplication, QWidget
from rocketwidget import RocketWidget
from main_window import MainWindow
from qmessage_box import Widget
from qpush import Qpush
from qline import Qline
from qtextedit import Qtext
from qlabel import Qlab
from size_policy import Widget
from grid_layout import Gridlay
from qcheck_box_and_radio import Qchk
import sys
# sys module provides access to some variables used or
#  maintained by the interpreter and to functions that
#  interact strongly with the interpreter. It is always available.
print(sys.argv)
# sys.argv is a list in Python, which contains the command-line arguments passed to the script.
# QApplication is the main application class. It handles the initialization and finalization of the GUI application.
app=QApplication(sys.argv)

#window=MainWindow(app)
#window=RocketWidget(app)
#window=Widget()
#window=Qpush()
#window=Qline()
#window=Qtext()
#window=Qlab()
#window=Widget()
#window=Gridlay()
window=Qchk()
# QWidget is the base class of all user 
# interface objects in PyQt5. It provides default functionality and
#  a constructor for all user interface objects.
window.show()
# The show() method displays the widget on the screen.
app.exec()
# The exec() method executes the application,

