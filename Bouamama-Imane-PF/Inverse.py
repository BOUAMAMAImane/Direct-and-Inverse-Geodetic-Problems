from math import *
from main import calcul_rayon_Gauss as Rg
import Conversion
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from math import *
import Conversion
import main
import mpmath as mp

class Ui_Form11(object):
    def function(self):
        if self.comboBox_2.currentText() == "WGS 84":
            a=6378137
            b=6356752.314
            E = 4 * ((b * b) *pi* 1.00449)
        elif self.comboBox_2.currentText() == "Clarck 1880":
            a=6378249.20
            b=6356515.0
            E = 4 * ((b * b) *pi* 1.00456)

        if self.comboBox_3.currentText() == "calcul_rayon_v":
            R=main.calcul_rayon_v(a,b)

        elif self.comboBox_3.currentText() == "calcul_rayon_Gauss":
            R=main.calcul_rayon_Gauss(a,b)

        elif self.comboBox_3.currentText() == "calcul_rayon_a":
            R=main.calcul_rayon_a(E)

        elif self.comboBox_3.currentText() == "calcul_rayon_moyen":
            R=main.calcul_rayon_moyen(a,b)

        phi1d = float(self.lineEdit.text())
        phi1m = float(self.lineEdit_2.text())
        phi1s = float(self.lineEdit_3.text())
        phi2d = float(self.lineEdit_14.text())
        phi2m = float(self.lineEdit_7.text())
        phi2s = float(self.lineEdit_15.text())

        lambda1d = float(self.lineEdit_4.text())
        lambda1m = float(self.lineEdit_5.text())
        lambda1s = float(self.lineEdit_6.text())
        lambda2d = float(self.lineEdit_23.text())
        lambda2m = float(self.lineEdit_22.text())
        lambda2s = float(self.lineEdit_24.text())
        phi1=Conversion.dmstorad(phi1d,phi1m,phi1s)
        phi2 = Conversion.dmstorad(phi2d, phi2m, phi2s)
        lambda1= Conversion.dmstorad(lambda1d,lambda1m,lambda1s)
        lambda2 = Conversion.dmstorad(lambda2d, lambda2m, lambda2s)
        delta_lambda=lambda1-lambda2
        #DETERMINATION DE SIGMA12
        #sigma12=acos(sin(phi1)*sin(phi2)+cos(phi1)*cos(phi2)*cos(delta_lambda))*(180/pi)
        sigma12 = acos((sin(phi1) * sin(phi2) + cos(phi1) * cos(phi2) * cos(delta_lambda)))
        dis_ang_metre = sigma12 *R
        #print(dis_ang_metre)
        #DETRMINATION DE A12
        cot1= (tan(phi2)*cos(phi1)/sin(delta_lambda)) - (sin(phi1)*mp.cot(delta_lambda))
        A12=mp.acot(cot1)
        (A12_d, A12_m, A12_s) = Conversion.radtodms(A12)
        #DETERMINATION D'AZIMUT DE RETOUR
        A21=(mp.acot(-((tan(phi1)*cos(phi2)/sin(delta_lambda))-sin(phi2)*mp.cot(delta_lambda))))
        (A21_d, A21_m, A21_s) = Conversion.radtodms(A21)

        self.lineEdit_20.setText(str(A12_d))
        self.lineEdit_19.setText(str(A12_m))
        self.lineEdit_21.setText(str(A12_s))

        self.lineEdit_17.setText(str(A21_d))
        self.lineEdit_18.setText(str(A21_m))
        self.lineEdit_16.setText(str(A21_s))

        self.lineEdit_25.setText(str(dis_ang_metre))
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(840, 377)
        Form.setStyleSheet(u"background-color: rgb(171, 180, 255);")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(8, 134, 91, 21))
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(176, 135, 16, 16))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(251, 134, 16, 16))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(330, 134, 16, 16))
        self.label_5.setFont(font1)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(370, 310, 101, 41))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.label_17 = QLabel(Form)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(80, 20, 271, 51))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.label_17.setFont(font3)
        self.label_17.setStyleSheet(u"color: rgb(170, 0, 0);\n"
"color: rgb(0, 0, 127);")
        self.label_24 = QLabel(Form)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(675, 133, 16, 16))
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(177, 176, 16, 16))
        self.label_11.setFont(font1)
        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(332, 175, 16, 16))
        self.label_13.setFont(font1)
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(253, 176, 16, 16))
        self.label_12.setFont(font1)
        self.lineEdit_6 = QLineEdit(Form)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(269, 175, 57, 19))
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(114, 176, 57, 19))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(193, 134, 56, 19))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(8, 179, 101, 16))
        self.label_10.setFont(font)
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(269, 134, 57, 19))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(114, 133, 57, 20))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_5 = QLineEdit(Form)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(193, 176, 56, 19))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_16 = QLineEdit(Form)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setGeometry(QRect(720, 228, 91, 20))
        self.lineEdit_16.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(704, 228, 16, 16))
        self.label_16.setFont(font1)
        self.label_27 = QLabel(Form)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(433, 230, 71, 16))
        self.label_27.setFont(font)
        self.lineEdit_17 = QLineEdit(Form)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setGeometry(QRect(531, 228, 71, 20))
        self.lineEdit_17.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_18 = QLineEdit(Form)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setGeometry(QRect(630, 228, 71, 19))
        self.lineEdit_18.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_25 = QLabel(Form)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(610, 230, 16, 16))
        self.label_26 = QLabel(Form)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(817, 230, 16, 16))
        font4 = QFont()
        font4.setPointSize(10)
        self.label_26.setFont(font4)
        self.label_28 = QLabel(Form)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(816, 182, 16, 16))
        self.label_28.setFont(font4)
        self.lineEdit_19 = QLineEdit(Form)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setGeometry(QRect(629, 180, 71, 20))
        self.lineEdit_19.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_20 = QLineEdit(Form)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setGeometry(QRect(530, 180, 71, 20))
        self.lineEdit_20.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_29 = QLabel(Form)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(609, 182, 16, 16))
        self.label_30 = QLabel(Form)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(703, 180, 16, 16))
        self.label_30.setFont(font1)
        self.lineEdit_21 = QLineEdit(Form)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setGeometry(QRect(719, 180, 91, 20))
        self.lineEdit_21.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_31 = QLabel(Form)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(432, 182, 71, 16))
        self.label_31.setFont(font)
        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(9, 220, 91, 21))
        self.label_14.setFont(font)
        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(177, 221, 16, 16))
        self.label_15.setFont(font1)
        self.label_22 = QLabel(Form)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(331, 220, 16, 16))
        self.label_22.setFont(font1)
        self.lineEdit_7 = QLineEdit(Form)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(194, 220, 56, 19))
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_23 = QLabel(Form)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(252, 220, 16, 16))
        self.label_23.setFont(font1)
        self.lineEdit_14 = QLineEdit(Form)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setGeometry(QRect(115, 219, 57, 20))
        self.lineEdit_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_15 = QLineEdit(Form)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setGeometry(QRect(270, 220, 57, 19))
        self.lineEdit_15.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_32 = QLabel(Form)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(9, 260, 91, 21))
        self.label_32.setFont(font)
        self.label_33 = QLabel(Form)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(177, 261, 16, 16))
        self.label_33.setFont(font1)
        self.label_34 = QLabel(Form)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(331, 260, 16, 16))
        self.label_34.setFont(font1)
        self.lineEdit_22 = QLineEdit(Form)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setGeometry(QRect(194, 260, 56, 19))
        self.lineEdit_22.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_35 = QLabel(Form)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(252, 260, 16, 16))
        self.label_35.setFont(font1)
        self.lineEdit_23 = QLineEdit(Form)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setGeometry(QRect(115, 259, 57, 20))
        self.lineEdit_23.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_24 = QLineEdit(Form)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setGeometry(QRect(270, 260, 57, 19))
        self.lineEdit_24.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_36 = QLabel(Form)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(432, 133, 141, 20))
        self.label_36.setFont(font)

        self.lineEdit_25 = QLineEdit(Form)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setGeometry(QRect(577, 133, 91, 20))
        self.lineEdit_25.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(400, 30, 141, 31))
        font5 = QFont()
        font5.setKerning(False)
        self.comboBox_2.setFont(font5)
        self.comboBox_2.setAcceptDrops(True)
        self.comboBox_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.comboBox_3 = QComboBox(Form)
        self.comboBox_3.addItem(u"calcul_rayon_v")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(570, 30, 211, 31))
        self.comboBox_3.setFont(font5)
        self.comboBox_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton.clicked.connect(self.function)
        #self.pushButton.clicked.connect(self.function)
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Latitude de P1", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u00b0", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"'", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\"", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Convertir", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Probl\u00e8me Inverse Sur La Sph\u00e8re", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"m", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u00b0", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\"", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"'", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Longitude de P1", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"'", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"Azimut A21", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"\u00b0", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"\"", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"\"", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"\u00b0", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"'", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"Azimut A12", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Latitude de P2", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u00b0", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"\"", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"'", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"Longitude de P2", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"\u00b0", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"\"", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"'", None))
        self.label_36.setText(QCoreApplication.translate("Form", u"Distance entre P1 et P2", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"Clarck 1880", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"WGS 84", None))

        self.comboBox_3.setItemText(1, QCoreApplication.translate("Form", u"calcul_rayon_Gauss", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Form", u"calcul_rayon_moyen", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Form", u"calcul_rayon_a", None))

    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())