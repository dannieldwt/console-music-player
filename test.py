#!/usr/bin/env python
# encoding: utf-8
'''
@author: Danniel
@license: (C) Copyright
@contact: 1085837135@qq.com
@software: PyCharm
@file: test.py
@time: 2019-04-13 18:29
@desc:
该文件是在项目创立时候（可能以后维护更新的时候仍会使用）的
测试文件，用于测试每个模块的运行状态
'''

import logging
from order_line_parser.parser import parser_command

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='console-music-player.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)


while True:
    command = input(">>: ")
    parser_bool, parser_result = parser_command(command)
    print("parser_bool: ", parser_bool)
    print("parser_result: ", parser_result)


