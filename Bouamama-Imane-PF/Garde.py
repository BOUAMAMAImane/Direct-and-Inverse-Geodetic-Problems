from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from menuprincipale import Ui_Form5



class Ui_Form(object):
    def open_5(self):
      self.formSecond = QtWidgets.QWidget()
      self.ui = Ui_Form5()
      self.ui.setupUi(self.formSecond)
      self.formSecond.show()

    # window.close()

    def setupUi(self, Form):
        if not Form.objectName():
         Form.setObjectName(u"Form")
        Form.resize(772, 495)
        Form.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 90, 481, 311))
        self.label.setStyleSheet(u"background-color: rgb(156, 169, 255);")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(310, 10, 201, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 40, 361, 51))
        self.label_3.setFont(font)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 450, 161, 21))
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(True)
        self.label_6.setFont(font1)
        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(340, 420, 111, 51))
        self.pushButton_7.setStyleSheet(u"background- color: rgb(255, 255, 255);")
        #self.pushButton_7.clicked.connect(self.open1)
        self.pushButton_7.clicked.connect(self.open_5)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><img src=\"image1.png\"/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Bienvenue ", None))
        self.label_3.setText(QCoreApplication.translate("Form", u" Convertisseur de coordonn\u00e9es ", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"BOUAMAMA Imane  Geo/S3", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"Commencer", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form= QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
