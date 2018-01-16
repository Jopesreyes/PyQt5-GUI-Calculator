from PyQt5 import QtWidgets
from Ui_Calculator import Ui_calculator

class CalculatorWindow(QtWidgets.QMainWindow, Ui_calculator):
    firstNum = None
    userIsTypingSecondNumber = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton_0.clicked.connect(self.digit_pressed)
        self.pushButton_1.clicked.connect(self.digit_pressed)
        self.pushButton_2.clicked.connect(self.digit_pressed)
        self.pushButton_3.clicked.connect(self.digit_pressed)
        self.pushButton_4.clicked.connect(self.digit_pressed)
        self.pushButton_5.clicked.connect(self.digit_pressed)
        self.pushButton_6.clicked.connect(self.digit_pressed)
        self.pushButton_7.clicked.connect(self.digit_pressed)
        self.pushButton_8.clicked.connect(self.digit_pressed)
        self.pushButton_9.clicked.connect(self.digit_pressed)

        self.pushButton_decimal.clicked.connect(self.decimal_pressed)

        self.pushButton_percent.clicked.connect(self.unary_operation_pressed)

        self.pushButton_plus.clicked.connect(self.binary_btns_clicked)
        self.pushButton_minus.clicked.connect(self.binary_btns_clicked)
        self.pushButton_divide.clicked.connect(self.binary_btns_clicked)
        self.pushButton_multiply.clicked.connect(self.binary_btns_clicked)
        self.pushButton_equal.clicked.connect(self.equals_btn_clicked)
        self.pushButton_clear.clicked.connect(self.clear_btn_clicked)
        self.pushButton_backspace.clicked.connect(self.backspace_btn_clicked)

        self.pushButton_plus.setCheckable(True)
        self.pushButton_minus.setCheckable(True)
        self.pushButton_divide.setCheckable(True)
        self.pushButton_multiply.setCheckable(True)

    def digit_pressed(self):
        button = self.sender()
        if ((self.pushButton_plus.isChecked() or self.pushButton_minus.isChecked() or
                self.pushButton_divide.isChecked() or self.pushButton_multiply.isChecked()) and
                (not self.userIsTypingSecondNumber)):
            newLabel = format(float(button.text()), '.15g')
            self.userIsTypingSecondNumber = True
        else:
            if (('.' in self.label.text()) and (button.text() == '0')):
                newLabel = format(self.label.text() + button.text(), '.15')
            else:
                newLabel = format(float(self.label.text() + button.text()), '.15g')
        self.label.setText(newLabel)

    def decimal_pressed(self):
        if ('.' in self.label.text()):
            newLabel = self.label.setText(self.label.text())
        else:
            newLabel = self.label.setText(self.label.text() + '.')

    def unary_btn_clicked(self):
        button = self.sender()

        labelNumber = float(self.label.text())
        if button.text() == '%':
            labelNumber = labelNumber * 0.01
        newLabel = format(labelNumber, '.15g')
        self.label.setText(newLabel)

    def binary_btns_clicked(self):
        button = self.sender()

        self.firstNum = float(self.label.text())

        button.setChecked(True)

    def equals_btn_clicked(self):
        secondNum = float(self.label.text())
        if self.pushButton_plus.isChecked():
            labelNumber = self.firstNum + secondNum
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_plus.setChecked(False)

        elif self.pushButton_minus.isChecked():
            labelNumber = self.firstNum - secondNum
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_minus.setChecked(False)

        elif self.pushButton_divide.isChecked():
            labelNumber = self.firstNum / secondNum
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_divide.setChecked(False)

        elif self.pushButton_multiply.isChecked():
            labelNumber = self.firstNum * secondNum
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_multiply.setChecked(False)

            self.userIsTypingSecondNumber = False

    def clear_btn_clicked(self):
        self.pushButton_plus.setChecked(False)
        self.pushButton_minus.setChecked(False)
        self.pushButton_divide.setChecked(False)
        self.pushButton_multiply.setChecked(False)

        self.userIsTypingSecondNumber = False
        self.label.setText('0')

    def backspace_btn_clicked(self):
        newLabel = self.label.text()[:-1]
        self.label.setText(newLabel)
