def Convertion(a,b,c):
    PI = 3.14
    Deg=a+(b+c/60)/60
    Rad=Deg*PI/180
    return Rad
#d=int(input("entrer la partie deegree:"))
#m=int(input("entrer la partie minute:"))
#s=int(input("entrer la partie seconde:"))
#print(Convert(d,m,s))

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
