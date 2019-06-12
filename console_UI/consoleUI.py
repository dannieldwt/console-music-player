# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'console-UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from console_UI.cmd import cmd_UI

class Ui_console_main_window(object):
    def setupUi(self, console_main_window):
        console_main_window.setObjectName("console_main_window")
        console_main_window.resize(800, 616)
        self.console_central_widget = QtWidgets.QWidget(console_main_window)
        self.console_central_widget.setObjectName("console_central_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.console_central_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.console_central_widget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.console = cmd_UI(self.splitter)
        self.console.setStyleSheet("background-color: rgb(0, 0, 0);color: rgb(0, 255, 127);")
        self.console.setObjectName("console")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        console_main_window.setCentralWidget(self.console_central_widget)

        self.retranslateUi(console_main_window)
        QtCore.QMetaObject.connectSlotsByName(console_main_window)

    def retranslateUi(self, console_main_window):
        _translate = QtCore.QCoreApplication.translate
        console_main_window.setWindowTitle(_translate("console_main_window", "MainWindow"))


