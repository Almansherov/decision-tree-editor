import sys

from PySide2.QtWidgets import QApplication, QLabel


app = QApplication(sys.argv)

#label = QLabel("Hello World!")

label = QLabel("<font color=red size=40>All right, I don't have any fucking idea what I am doing!</font>")

label.show()

app.exec_()

