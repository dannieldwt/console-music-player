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
from PyQt5 import *
from order_line_parser.parser import *

class cmd_UI(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        insert_text = ">>: "
        self.insertPlainText(insert_text)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            #调用命令解析层，并返回执行结果信息
            #parser_singleton = Parser()
            #parser_result = parser_singleton.parser_command()
            insert_text = ">>: "
            lines = self.document().lineCount()
            command_raw = self.document().findBlockByLineNumber(lines - 1).text()
            command = command_raw[4:]
            parser_singleton = Parser()
            parser_bool, parser_result = parser_singleton.parser_command(command)
            self.appendPlainText(parser_result)
            super().keyPressEvent(event)
            self.insertPlainText(insert_text)
        else:
            super().keyPressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cmd = cmd_UI()
    cmd.show()
    sys.exit(app.exec_())