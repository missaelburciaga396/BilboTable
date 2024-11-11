# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BilboMainView.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHeaderView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

from ViewModel.BilboMainViewModel import BilboMainViewModel

db_path = "DB/BilboDb.db"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.ViewModel = BilboMainViewModel(db_path)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableViewBilbo = QTableView(self.centralwidget)
        self.tableViewBilbo.setObjectName(u"tableViewBilbo")
        self.tableViewBilbo.setGeometry(QRect(140, 50, 631, 501))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 299, 121, 141))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnAgregar = QPushButton(self.verticalLayoutWidget)
        self.btnAgregar.setObjectName(u"btnAgregar")
        self.btnAgregar.clicked.connect(self.ViewModel.registrar_widget)
        self.verticalLayout.addWidget(self.btnAgregar)

        self.btnEliminar = QPushButton(self.verticalLayoutWidget)
        self.btnEliminar.setObjectName(u"btnEliminar")

        self.verticalLayout.addWidget(self.btnEliminar)

        self.btnEditar = QPushButton(self.verticalLayoutWidget)
        self.btnEditar.setObjectName(u"btnEditar")

        self.verticalLayout.addWidget(self.btnEditar)

        self.btnGudardar = QPushButton(self.verticalLayoutWidget)
        self.btnGudardar.setObjectName(u"btnGudardar")

        self.verticalLayout.addWidget(self.btnGudardar)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 50, 111, 131))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBoxDominadas = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBoxDominadas.setObjectName(u"checkBoxDominadas")

        self.verticalLayout_2.addWidget(self.checkBoxDominadas)

        self.checkBoxFondos = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBoxFondos.setObjectName(u"checkBoxFondos")

        self.verticalLayout_2.addWidget(self.checkBoxFondos)

        self.checkBoxPistolsquad = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBoxPistolsquad.setObjectName(u"checkBoxPistolsquad")

        self.verticalLayout_2.addWidget(self.checkBoxPistolsquad)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnAgregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.btnEliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.btnEditar.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btnGudardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.checkBoxDominadas.setText(QCoreApplication.translate("MainWindow", u"Dominadas", None))
        self.checkBoxFondos.setText(QCoreApplication.translate("MainWindow", u"Fondos", None))
        self.checkBoxPistolsquad.setText(QCoreApplication.translate("MainWindow", u"Pistolsquad", None))
    # retranslateUi

