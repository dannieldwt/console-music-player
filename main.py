#!/usr/bin/env python
# encoding: utf-8
'''
@author: 10858
@license: (C) Copyright
@contact: xxx@qq.com
@software: PyCharm
@file: main.py
@time: 2019-06-12 10:52
@desc:
执行文件
'''

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from console_UI.cmd import cmd_UI
from console_UI.consoleUI import Ui_console_main_window
from PyQt5.QtWidgets import *



app = QApplication(sys.argv)
mainwindow = QMainWindow()
UI = Ui_console_main_window()
UI.setupUi(mainwindow)
#mainwindow.setStyleSheet("background-color: rgb(0, 0, 0);color: rgb(0, 255, 127);")
mainwindow.show()
sys.exit(app.exec_())