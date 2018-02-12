from PyQt5 import QtWidgets
from MyCalculator import Ui_Calculator

class mycalculator(QtWidgets.QMainWindow, Ui_Calculator):
    firstNum = None
    SecondNumType = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton_0.clicked.connect(self.button_pressed)
        self.pushButton_1.clicked.connect(self.button_pressed)
        self.pushButton_2.clicked.connect(self.button_pressed)
        self.pushButton_3.clicked.connect(self.button_pressed)
        self.pushButton_4.clicked.connect(self.button_pressed)
        self.pushButton_5.clicked.connect(self.button_pressed)
        self.pushButton_6.clicked.connect(self.button_pressed)
        self.pushButton_7.clicked.connect(self.button_pressed)
        self.pushButton_8.clicked.connect(self.button_pressed)
        self.pushButton_9.clicked.connect(self.button_pressed)

        self.pushButton_plus.clicked.connect(self.binary_button_pressed)
        self.pushButton_minus.clicked.connect(self.binary_button_pressed)
        self.pushButton_multiply.clicked.connect(self.binary_button_pressed)
        self.pushButton_divide.clicked.connect(self.binary_button_pressed)

        self.pushButton_decimal.clicked.connect(self.decimal_pressed)

        self.pushButton_clear.clicked.connect(self.clear_button_pressed)

        self.pushButton_equal.clicked.connect(self.equal_pressed)

        self.pushButton_backspace.clicked.connect(self.backspace_pressed)

        self.pushButton_plus.setCheckable(True)
        self.pushButton_minus.setCheckable(True)
        self.pushButton_multiply.setCheckable(True)
        self.pushButton_divide.setCheckable(True)


    def button_pressed(self):
        button = self.sender()
        if ((self.pushButton_plus.isChecked() or self.pushButton_minus.isChecked() or
                self.pushButton_multiply.isChecked() or self.pushButton_divide.isChecked())
                and (not self.SecondNumType)):
            newLabel = format(float(button.text()), '.20g')
            self.SecondNumType = True
        else:
            if (('.' in self.label.text()) and (button.text == '0')):
                newLabel = format(float(self.label.text() + button.text()), '.20')
            else:
                newLabel = format(float(self.label.text() + button.text()), '.20g')
        self.label.setText(newLabel)

    def binary_button_pressed(self):
        button = self.sender()
        self.firstNum = float(self.label.text())

        button.setChecked(True)

    def decimal_pressed(self):
        if ('.' in self.label.text()):
            newLabel = self.label.setText(self.label.text())
        else:
            newLabel = self.label.setText(self.label.text() + '.')


    def clear_button_pressed(self):
        self.pushButton_plus.setChecked(False)
        self.pushButton_minus.setChecked(False)
        self.pushButton_divide.setChecked(False)
        self.pushButton_multiply.setChecked(False)

        self.SecondNumType = False
        self.label.setText('0')

    def equal_pressed(self):
        secondNum = float(self.label.text())
        if self.pushButton_plus.isChecked():
            labelNumber = self.firstNum + secondNum
            newLabel = format(labelNumber, '.20g')
            self.label.setText(newLabel)
            self.pushButton_plus.setChecked(False)

        elif self.pushButton_minus.isChecked():
            labelNumber = self.firstNum - secondNum
            newLabel = format(labelNumber, '.20g')
            self.label.setText(newLabel)
            self.pushButton_minus.setChecked(False)

        elif self.pushButton_divide.isChecked():
            labelNumber = self.firstNum / secondNum
            newLabel = format(labelNumber, '.20g')
            self.label.setText(newLabel)
            self.pushButton_divide.setChecked(False)

        elif self.pushButton_multiply.isChecked():
            labelNumber = self.firstNum * secondNum
            newLabel = format(labelNumber, '.20g')
            self.label.setText(newLabel)
            self.pushButton_multiply.setChecked(False)

            self.SecondNumType = False

    def backspace_pressed(self):
        newLabel = self.label.text()[:-1]
        self.label.setText(newLabel)
