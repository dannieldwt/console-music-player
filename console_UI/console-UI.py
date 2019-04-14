# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'console-UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from console_UI.cmd import cmd_UI
from PyQt5.QtWidgets import *

class Ui_console_main_window(object):
    def setupUi(self, console_main_window):
        console_main_window.setObjectName("console_main_window")
        console_main_window.resize(800, 600)
        self.console_central_widget = QtWidgets.QWidget(console_main_window)
        self.console_central_widget.setObjectName("console_central_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.console_central_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.console = cmd_UI(self.console_central_widget)
        self.console.setObjectName("console")
        self.gridLayout.addWidget(self.console, 0, 0, 1, 1)
        console_main_window.setCentralWidget(self.console_central_widget)
        self.menubar = QtWidgets.QMenuBar(console_main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        console_main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(console_main_window)
        self.statusbar.setObjectName("statusbar")
        console_main_window.setStatusBar(self.statusbar)

        self.retranslateUi(console_main_window)
        QtCore.QMetaObject.connectSlotsByName(console_main_window)

    def retranslateUi(self, console_main_window):
        _translate = QtCore.QCoreApplication.translate
        console_main_window.setWindowTitle(_translate("console_main_window", "MainWindow"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    UI = Ui_console_main_window()
    UI.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())

