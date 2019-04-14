#!/usr/bin/env python
# encoding: utf-8
'''
@author: 10858
@license: (C) Copyright
@contact: xxx@qq.com
@software: PyCharm
@file: cmd.py
@time: 2019-04-14 16:23
@desc:
'''

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class cmd_UI(QPlainTextEdit):
    def __init__(self, parent):
        super().__init__(parent=None)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            test_str = "test"
            self.insertPlainText(test_str)
        super().keyPressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cmd = cmd_UI()
    cmd.show()
    sys.exit(app.exec_())