import sys
from PyQt5.QtWidgets import QApplication
from Calculator import mycalculator

app = QApplication(sys.argv)

calculator = mycalculator()

sys.exit(app.exec_())