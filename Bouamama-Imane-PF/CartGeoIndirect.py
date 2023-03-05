from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import math
import Conv
import numpy as np
import Rad
from PyQt5 import QtWidgets

class Ui_Form3(object):

    def cartesienneGeo(self):
        a = 6378249.145
        b = 6356514.39
        X = float(self.lineEdit_8.text())
        Y = float(self.lineEdit_9.text())
        Z = float(self.lineEdit_10.text())
        e2 = 1 - (b / a) ** 2

        landa = np.arctan(Y / X)

        phi0 = np.arctan(Z / np.sqrt(X ** 2 + Y ** 2) * (1 + (e2 / (1 - e2))))
        N0 = a / np.sqrt(1 - (e2 * np.sin(phi0) ** 2))

        phi_i = np.arctan(Z / np.sqrt(X ** 2 + Y ** 2) * (1 + (e2 * N0 * np.sin(phi0) / (Z))))
        N_i = a / np.sqrt(1 - (e2 * np.sin(phi0) ** 2))
        err = 0.00000001

        while (abs(phi_i - phi0) < err):
            phi0 = phi_i
            N0 = N_i
            phi_i = np.arctan(Z / np.sqrt(X ** 2 + Y ** 2) * (1 + (e2 * N0 * np.sin(phi0) / (Z))))
        # print(phi_i)

        phi = phi_i

        h = (math.sqrt(X ** 2 + Y ** 2)) * np.cos(phi) + (Z * np.sin(phi)) - a * math.sqrt(1 - (e2 * np.sin(phi) ** 2))

        (phid, phim, phis) = Conv.Convertion(phi)
        (landad, landam, landas) = Conv.Convertion(landa)
        self.lineEdit.setText(str(phid))
        self.lineEdit_2.setText(str(phim))
        self.lineEdit_3.setText(str(phis))

        self.lineEdit_4.setText(str(landad))
        self.lineEdit_5.setText(str(landam))
        self.lineEdit_6.setText(str(landas))

        self.lineEdit_7.setText(str(h))

    ###################################################################33
    def CartGeo(self):
        f = 1 / 293.46602
        e_2 = 0.0068034876
        a = 6378249.20
        X = float(self.lineEdit_8.text())
        Y = float(self.lineEdit_9.text())
        Z = float(self.lineEdit_10.text())

        r = math.sqrt(X ** 2 + Y ** 2 + Z ** 2)

        mu = np.arctan((Z / (np.sqrt(X ** 2 + Y ** 2))) * ((1 - f) + ((a * e_2) / r)))
        Long= np.arctan(Y / X)
        Lat = np.arctan((Z * (1 - f) + e_2 * a * np.sin(mu) ** 3) / (
                (1 - f) * (math.sqrt(X ** 2 + Y ** 2) - (e_2 * a * np.cos(mu) ** 3))))
        h = (math.sqrt(X ** 2 + Y ** 2)) * math.cos(Lat) + (Z * math.sin(Lat)) - a * math.sqrt(
            1 - (e_2 * math.sin(Lat) ** 2))
        (d1, m1, s1) = Convertion.Conv(Long)
        (d2, m2, s2) = Convertion.Conv(Lat)

        self.lineEdit.setText(str(d2))
        self.lineEdit_2.setText(str(m2))
        self.lineEdit_3.setText(str(s2))

        self.lineEdit_4.setText(str(d1))
        self.lineEdit_5.setText(str(m1))
        self.lineEdit_6.setText(str(s1))

        self.lineEdit_7.setText(str(h))

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(736, 302)
        Form.setStyleSheet(u"background-color: rgb(190, 194, 255);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 60, 241, 41))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 0, 127);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 128, 71, 20))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(450, 130, 16, 16))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(550, 130, 16, 16))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_4.setFont(font2)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(660, 130, 16, 16))
        self.label_5.setFont(font2)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 240, 111, 41))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_17 = QLabel(Form)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 10, 681, 41))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.label_17.setFont(font4)
        self.label_17.setStyleSheet(u"color: rgb(170, 0, 0);\n"
"color: rgb(0, 0, 127);")
        self.label_23 = QLabel(Form)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(41, 124, 17, 16))
        font5 = QFont()
        font5.setPointSize(9)
        font5.setBold(False)
        self.label_23.setFont(font5)
        self.label_25 = QLabel(Form)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(41, 196, 16, 16))
        self.label_25.setFont(font1)
        self.label_24 = QLabel(Form)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(190, 124, 16, 16))
        self.label_26 = QLabel(Form)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(41, 160, 17, 16))
        self.label_26.setFont(font5)
        self.lineEdit_8 = QLineEdit(Form)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(62, 124, 97, 19))
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_10 = QLineEdit(Form)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(62, 196, 97, 19))
        self.lineEdit_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_9 = QLineEdit(Form)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(62, 160, 97, 19))
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(450, 163, 16, 16))
        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(660, 165, 16, 16))
        self.label_13.setFont(font2)
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(548, 166, 16, 16))
        self.label_12.setFont(font2)
        self.lineEdit_6 = QLineEdit(Form)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(560, 164, 91, 19))
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(371, 164, 71, 19))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(470, 128, 71, 20))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(290, 164, 81, 20))
        self.label_10.setFont(font1)
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(560, 128, 91, 19))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_7 = QLineEdit(Form)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(370, 200, 91, 20))
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(372, 128, 71, 19))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_5 = QLineEdit(Form)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(470, 164, 71, 19))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(290, 200, 71, 20))
        self.label_14.setFont(font1)
        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(470, 200, 16, 16))
        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(30, 60, 241, 41))
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"color: rgb(0, 0, 127);\n"
"color: rgb(0, 0, 0);")
        self.pushButton.clicked.connect(self.cartesienneGeo)
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Coordonn\u00e9es geographiques ", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Latitude (\u03c6)", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u00b0", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"'", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\"", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Convertir", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Transformation des coordonn\u00e9es cart\u00e9siennes  aux coordonn\u00e9es g\u00e9ographiques (It\u00e9rative)", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"X", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Z", None))
        self.label_24.setText("")
        self.label_26.setText(QCoreApplication.translate("Form", u"Y ", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u00b0", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\"", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"'", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Longitude(\u03bb)", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Hauteur(h)", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"m", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Coordonn\u00e9es cart\u00e9siennes", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form3()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

