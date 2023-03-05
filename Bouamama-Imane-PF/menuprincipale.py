from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Direct import Ui_Form10
from Inverse import Ui_Form11
from GeoCart4 import Ui_Form1
from CartGeoDirect import Ui_Form2
from CartGeoIndirect import Ui_Form3

class Ui_Form5(object):
    def open10(self):
        self.formSecond = QtWidgets.QWidget()
        self.ui = Ui_Form10()
        self.ui.setupUi(self.formSecond)
        self.formSecond.show()
        #window.close()

    def open11(self):
        self.formSecond = QtWidgets.QWidget()
        self.ui = Ui_Form11()
        self.ui.setupUi(self.formSecond)
        self.formSecond.show()
        #window.close()
    def open1(self):
        self.formSecond = QtWidgets.QWidget()
        self.ui = Ui_Form1()
        self.ui.setupUi(self.formSecond)
        self.formSecond.show()
        #window.close()
    def open2(self):
        self.formSecond = QtWidgets.QWidget()
        self.ui = Ui_Form2()
        self.ui.setupUi(self.formSecond)
        self.formSecond.show()
        #window.close()
    def open3(self):
        self.formSecond = QtWidgets.QWidget()
        self.ui = Ui_Form3()
        self.ui.setupUi(self.formSecond)
        self.formSecond.show()
        #window.close()
    def setupUi(self, Form):
        if not Form.objectName():
         Form.setObjectName(u"Form")
        Form.resize(765, 476)
        Form.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 20, 361, 51))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_3.setFont(font)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(420, 100, 91, 41))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton.clicked.connect(self.open2)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(565, 99, 91, 41))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_2.clicked.connect(self.open3)
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(420, 176, 91, 41))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_3.clicked.connect(self.open1)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(63, 90, 321, 51))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 177, 321, 41))
        self.label_5.setFont(font1)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(63, 250, 321, 51))
        self.label_7.setFont(font1)
        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(64, 310, 91, 41))
        self.pushButton_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_5.clicked.connect(self.open10)
        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(250, 310, 91, 41))
        self.pushButton_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_7.clicked.connect(self.open11)

        font2 = QFont()
        font2.setKerning(False)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Menu Convertisseur de coordonn\u00e9es ", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Directe", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Iterative", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Convertir", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Coordonn\u00e9es Cartesiennes vers Geographique", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Coordonn\u00e9es geographique vers Cartesiennes", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Probl\u00e8mes sur la Sph\u00e8re", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Directe", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"Inverse", None))


    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form= QtWidgets.QWidget()
    ui = Ui_Form5()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
