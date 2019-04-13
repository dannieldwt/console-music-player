#!/usr/bin/env python
# encoding: utf-8
'''
@author: Danniel
@license: (C) Copyright
@contact: 1085837135@qq.com
@software: PyCharm
@file: parser.py
@time: 2019-04-13 17:20
@desc: 该文件属于解析层，包含了解析命令的函数
和UI层以及服务层相连接，为UI层调用，并调用服务层提供的服务
'''

import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='console-music-player.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

def parser_command(command):
    '''
    :desc: 该函数用于解析命令行的命令，是解析层的核心函数，参数为用户输入的一行命令，
    将命令依照命令表进行解析，并调用服务层的相应服务。返回值为运行结果。
    :param command: 字符串类型，为ui层传入，用户输入的一行命令，其中参数之间用空格隔开
    :return:
    parser_bool 返回一个bool类型表明是否出错
    parser_result 返回一个字符串，表示命令解析的结果，正常解析或者解析错误
    '''
    parser_result = ""
    parser_bool = True
    if len(command) == 0:
        logging.info("command is empty")
        parser_result = "PARSER ERROR: command is empty."
        parser_bool = False
        return parser_bool, parser_result

    command_terms = command.split(' ')
    command_terms_len = len(command_terms)
    if command_terms[0] == 'play':
        logging.info("command is parsered--play")
        if command_terms_len == 1:
            #如果当前没有音乐则表示播放失败，无音乐
            #否则播放当前音乐
            # play_bool, msg = play()
            parser_result = "PARSER SUCCESS: %s" % (command)
            parser_bool = True
            logging.info("command--play parser SUCCESS")
            return parser_bool, parser_result
        elif command_terms_len == 2:
            #播放所指定的歌名，如果歌名不存在报错(这是服务层的错误）
            #否则按照相应歌名进行播放
            parser_result = "PARSER SUCCESS: %s" % (command)
            parser_bool = True
            logging.info("command-play parser SUCCESS")
            return parser_bool, parser_result
        else:
            #参数超过三个，命令格式有错，解析失败
            parser_result = "PARSER ERROR: %s" % (command)
            parser_bool = False
            logging.info("command-play parser ERROR, too many arguments")
            return parser_bool, parser_result
    elif command_terms[0] == 'p':
        logging.info("command is parsered--p")
        if command_terms_len == 1:
            #播放上一首
            parser_result = "PARSER SUCCESS: %s" % (command)
            parser_bool = True
            logging.info("command-p parser SUCCESS")
            return parser_bool, parser_result
        else:
            #存在参数，命令格式错误，解析失败
            parser_result = "PARSER ERROR: %s" % (command)
            parser_bool = False
            logging.info("command-p parser ERROR, too many arguments")
            return parser_bool, parser_result
    elif command_terms[0] == 'n':
        logging.info("command is parsered--n")
        if command_terms_len == 1:
            #播放下一首
            parser_result = "PARSER SUCCESS: %s" % (command)
            parser_bool = True
            logging.info("command-n parser SUCCESS")
            return parser_bool, parser_result
        else:
            #存在参数， 命令格式有误， 解析失败
            parser_result = "PARSER ERROR: %s" % (command)
            parser_bool = False
            logging.info("command-n parser ERROR, too many arguments")
            return parser_bool, parser_result
    elif command_terms[0] == 'up':
        logging.info("command is parsered--up")
        if command_terms_len == 1:
            #没参数默认提高一个音量
            parser_result = "PARSER SUCCESS: %s" % (command)
            parser_bool = True
            logging.info("command-up parser SUCCESS")
            return parser_bool, parser_result
        elif command_terms_len == 2:
            if ~(command_terms[1].isdigit()):
                #输入不是纯数字，浮点数或者有字符
                parser_result = "PARSER ERROR: %s" % (command)
                parser_bool = False
                logging.info("command-up parser ERROR, value type")
                return parser_bool, parser_result
            voice = eval(command_terms[1])
            '''
            if voice > 100 or voice < 0:
                #输入的数值不在规范内
                parser_result = "PARSER ERROR: %s" % (command)
                parser_bool = False
                logging.info("command-up parser ERROR, value")
                return parser_bool, parser_result
            '''
            #调用服务层服务 设置音量
        else:
            #参数过多，命令不符合规范
            parser_result = "PARSER ERROR: %s" % (command)
            parser_bool = False
            logging.info("command-up parser ERROR, too many arguments")
            return parser_bool, parser_result
    elif command_terms[0] == 'down':
        logging.info("command is parsered--down")
        if command_terms_len == 1:
            # 没参数默认提高一个音量
            parser_result = "PARSER SUCCESS: %s" % (command)
            parser_bool = True
            logging.info("command-down parser SUCCESS")
            return parser_bool, parser_result
        elif command_terms_len == 2:
            if ~(command_terms[1].isdigit()):
                # 输入不是纯数字，浮点数或者有字符
                parser_result = "PARSER ERROR: %s" % (command)
                parser_bool = False
                logging.info("command-down parser ERROR, value type")
                return parser_bool, parser_result
            voice = eval(command_terms[1])
            '''
            if voice > 100 or voice < 0:
                #输入的数值不在规范内
                parser_result = "PARSER ERROR: %s" % (command)
                parser_bool = False
                logging.info("command-down parser ERROR, value")
                return parser_bool, parser_result
            '''
            # 调用服务层服务 设置音量
            parser_result = "PARSER SUCCESS: %s" % (command)
            parser_bool = True
            logging.info("command-down parser SUCCESS")
            return parser_bool, parser_result
        else:
            # 参数过多，命令不符合规范
            parser_result = "PARSER ERROR: %s" % (command)
            parser_bool = False
            logging.info("command-down parser ERROR, too many arguments")
            return parser_bool, parser_result
    elif command_terms[0] == "pause":
        logging.info("command is parsered--pause")
        if command_terms_len == 1:
            #命令格式正确，暂停正在播放的音乐
            parser_result = "PARSER SUCCESS %s" % (command)
            parser_bool = True
            logging.info("command-pause parser SUCCESS")
            return parser_bool, parser_result
        else:
            #参数过多，命令格式不符合规范
            parser_result = "PARSER ERROR: %s" % (command)
            parser_bool = False
            logging.info("command-pause parser ERROR, too many arguments")
            return parser_bool, parser_result
    elif command_terms[0] == "stop":
        logging.info("command is parsered--stop")
        if command_terms_len == 1:
            #命令格式正确，停止正在播放的音乐
            parser_result = "PARSER SUCCESS %s" % (command)
            parser_bool = True
            logging.info("command-stop parser SUCCESS")
            return parser_bool, parser_result
        else:
            #参数过多，命令格式不符合规范
            parser_result = "PARSER ERROR: %s" % (command)
            parser_bool = False
            logging.info("command-stop parser ERROR, too many arguments")
            return parser_bool, parser_result
    elif command_terms[0] == "lyric":
        logging.info("command is parsered--lyric")
        if command_terms_len == 1:
            #命令格式正确，显示歌词
            parser_result = "PARSER SUCCESS %s" % (command)
            parser_bool = True
            logging.info("command-lyric parser SUCCESS")
            return parser_bool, parser_result
        else:
            #参数过多，命令格式不符合规范
            parser_result = "PARSER ERROR: %s" % (command)
            parser_bool = False
            logging.info("command-lyric parser ERROR, too many arguments")
            return parser_bool, parser_result
    elif command_terms[0] == "mode":
        logging.info("command is parsered--mode")
        if command_terms_len == 1:
            parser_result = "PARSER SUCCESS %s" % (command)
            parser_bool = True
            logging.info("command-mode parser SUCCESS")
            return parser_bool, parser_result
        elif command_terms_len == 2:
            parser_result = "PARSER SUCCESS %s" % (command)
            parser_bool = True
            logging.info("command-mode parser SUCCESS")
            return parser_bool, parser_result
        else:
            # 参数过多，命令格式不符合规范
            parser_result = "PARSER ERROR: %s" % (command)
            parser_bool = False
            logging.info("command-mode parser ERROR, too many arguments")
            return parser_bool, parser_result
    elif command_terms[0] == "list":
        logging.info("command is parsered--list")
        if command_terms_len == 1:
            #mode顺序向下切换一个
            parser_result = "PARSER SUCCESS: %s" % (command)
            parser_bool = True
            logging.info("command-list parser SUCCESS")
            return parser_bool, parser_result
        elif command_terms_len == 2:
            #切换到指定模式
            parser_result = "PARSER SUCCESS: %s" % (command)
            parser_bool = True
            logging.info("command-list parser SUCCESS")
            return parser_bool, parser_result
        else:
            parser_result = "PARSER ERROR: %s" % (command)
            parser_bool = False
            logging.info("command-list parser ERROR, too many arguments")
            return parser_bool, parser_result
    elif command_terms[0] == "delete":
        logging.info("command is parsered--delete")
        if command_terms_len == 1:
            #删除当前正在播放的歌曲
            parser_result = "PARSER SUCCESS: %s" % (command)
            parser_bool = True
            logging.info("command-delete parser SUCCESS")
            return parser_bool, parser_result
        elif command_terms_len == 2:
            #删除指定了歌名的歌曲
            parser_result = "PARSER SUCCESS: %s" % (command)
            parser_bool = True
            logging.info("command-delete parser SUCCESS")
            return parser_bool, parser_result
        else:
            #命令格式不符合规范
            parser_result = "PARSER ERROR: %s" % (command)
            parser_bool = False
            logging.info("command-delete parser ERROR, too many arguments")
            return parser_bool, parser_result
    elif command_terms_len[0] == "pwd":
        logging.info("command is parsered--pwd")
        if command_terms_len == 1:
            #显示当前目录
            parser_result = "PARSER SUCCESS: %s" % (command)
            parser_bool = True
            logging.info("command-pwd parser SUCCESS")
            return parser_bool, parser_result
        elif command_terms_len == 2:
            #显示歌名对应的歌曲所在的目录
            parser_result = "PARSER SUCCESS: %s" % (command)
            parser_bool = True
            logging.info("command-pwd parser SUCCESS")
            return parser_bool, parser_result
        else:
            # 命令格式不符合规范
            parser_result = "PARSER ERROR: %s" % (command)
            parser_bool = False
            logging.info("command-pwd parser ERROR, too many arguments")
            return parser_bool, parser_result
    elif command_terms[0] == "cd":
        logging.info("command is parsered--cd")
        if command_terms_len == 2:
            #切换到指定目录
            parser_result = "PARSER SUCCESS: %s" % (command)
            parser_bool = True
            logging.info("command-pwd parser SUCCESS")
            return parser_bool, parser_result
        else:
            # 命令格式不符合规范
            parser_result = "PARSER ERROR: %s" % (command)
            parser_bool = False
            logging.info("command-pwd parser ERROR, too many or lack of arguments")
            return parser_bool, parser_result
    elif command_terms[0] == "quit":
        logging.info("command is parsered--quit")
        if command_terms_len == 1:
            #退出音乐播放器
            parser_result = "PARSER SUCCESS: %s" % (command)
            parser_bool = True
            logging.info("command-quit parser SUCCESS")
            return parser_bool, parser_result
        else:
            # 命令格式不符合规范
            parser_result = "PARSER ERROR: %s" % (command)
            parser_bool = False
            logging.info("command-quit parser ERROR, too many or lack of arguments")
            return parser_bool, parser_result
    else:
        #不存在的命令
        parser_result = "PARSER ERROR: %s" % (command)
        parser_bool = False
        logging.info("command parser ERROR, invalid command")