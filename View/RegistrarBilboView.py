# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegistrarBilboView.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(449, 457)
        self.verticalLayoutWidget = QWidget(widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(110, 110, 311, 261))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lblUserName = QLabel(self.verticalLayoutWidget)
        self.lblUserName.setObjectName(u"lblUserName")

        self.verticalLayout.addWidget(self.lblUserName)

        self.leUserName = QLineEdit(self.verticalLayoutWidget)
        self.leUserName.setObjectName(u"leUserName")

        self.verticalLayout.addWidget(self.leUserName)

        self.lblPesoCorporal = QLabel(self.verticalLayoutWidget)
        self.lblPesoCorporal.setObjectName(u"lblPesoCorporal")

        self.verticalLayout.addWidget(self.lblPesoCorporal)

        self.lePesoCorporal = QLineEdit(self.verticalLayoutWidget)
        self.lePesoCorporal.setObjectName(u"lePesoCorporal")

        self.verticalLayout.addWidget(self.lePesoCorporal)

        self.lblLastre = QLabel(self.verticalLayoutWidget)
        self.lblLastre.setObjectName(u"lblLastre")

        self.verticalLayout.addWidget(self.lblLastre)

        self.leLastre = QLineEdit(self.verticalLayoutWidget)
        self.leLastre.setObjectName(u"leLastre")

        self.verticalLayout.addWidget(self.leLastre)

        self.lblnumreps = QLabel(self.verticalLayoutWidget)
        self.lblnumreps.setObjectName(u"lblnumreps")

        self.verticalLayout.addWidget(self.lblnumreps)

        self.leNumReps = QLineEdit(self.verticalLayoutWidget)
        self.leNumReps.setObjectName(u"leNumReps")

        self.verticalLayout.addWidget(self.leNumReps)

        self.lbltipoEjercicio = QLabel(self.verticalLayoutWidget)
        self.lbltipoEjercicio.setObjectName(u"lbltipoEjercicio")

        self.verticalLayout.addWidget(self.lbltipoEjercicio)

        self.comboBoxEjercicio = QComboBox(self.verticalLayoutWidget)
        self.comboBoxEjercicio.addItem("")
        self.comboBoxEjercicio.addItem("")
        self.comboBoxEjercicio.addItem("")
        self.comboBoxEjercicio.addItem("")
        self.comboBoxEjercicio.addItem("")
        self.comboBoxEjercicio.setObjectName(u"comboBoxEjercicio")

        self.verticalLayout.addWidget(self.comboBoxEjercicio)

        self.btnOk = QDialogButtonBox(widget)
        self.btnOk.setObjectName(u"btnOk")
        self.btnOk.setGeometry(QRect(160, 390, 193, 28))
        self.btnOk.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"registrar", None))
        self.lblUserName.setText(QCoreApplication.translate("widget", u"Nombre de usuario:", None))
        self.lblPesoCorporal.setText(QCoreApplication.translate("widget", u"peso corporal en kg:", None))
        self.lblLastre.setText(QCoreApplication.translate("widget", u"lastre extra en kg:", None))
        self.lblnumreps.setText(QCoreApplication.translate("widget", u"numero de repes:", None))
        self.lbltipoEjercicio.setText(QCoreApplication.translate("widget", u"ejercicio:", None))
        self.comboBoxEjercicio.setItemText(0, QCoreApplication.translate("widget", u"Dominadas", None))
        self.comboBoxEjercicio.setItemText(1, QCoreApplication.translate("widget", u"Fondos", None))
        self.comboBoxEjercicio.setItemText(2, QCoreApplication.translate("widget", u"Pistolsquad/sentadilla a una pierna", None))
        self.comboBoxEjercicio.setItemText(3, QCoreApplication.translate("widget", u"lagartijas", None))
        self.comboBoxEjercicio.setItemText(4, QCoreApplication.translate("widget", u"australians", None))

    # retranslateUi

