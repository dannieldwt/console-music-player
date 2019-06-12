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

from music_player.Player import Player
from analyze.Analyze import Analyze

class Parser(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if Parser.__instance == None:
            Parser.__instance = object.__new__(Parser)
        return Parser.__instance

    def parser_command(self, command):
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
        player = Player()
        if len(command) == 0:
            parser_result = "PARSER ERROR: command is empty."
            parser_bool = False
            return parser_bool, parser_result

        command_terms = command.split(' ')
        command_terms_len = len(command_terms)
        if command_terms[0] == 'play':
            if command_terms_len == 1:
                #如果当前没有音乐则表示播放失败，无音乐
                #否则播放当前音乐
                service_bool, msg = player.play()
                parser_bool = True
                parser_msg = self.__parser_result_helper(parser_bool, msg, command)
                return parser_bool, parser_msg
            elif command_terms_len == 2:
                #播放所指定的歌名，如果歌名不存在报错(这是服务层的错误）
                #否则按照相应歌名进行播放
                service_bool, msg = player.play(command_terms[1])
                parser_bool = True
                parser_msg = self.__parser_result_helper(parser_bool, msg, command)
                return parser_bool, parser_msg
            else:
                #参数超过三个，命令格式有错，解析失败
                parser_bool = False
                parser_msg = self.__parser_result_helper(parser_bool, "参数过多，不符合命令规范", command)
                return parser_bool, parser_msg
        elif command_terms[0] == 'previous':
            if command_terms_len == 1:
                #播放上一首
                service_bool,msg = player.previous()
                parser_bool = True
                parser_result = self.__parser_result_helper(parser_bool, msg, command)
                return parser_bool, parser_result
            else:
                #存在参数，命令格式错误，解析失败
                parser_bool = False
                parser_result = self.__parser_result_helper(parser_bool, "参数过多，不符合命令规范" % (command))
                return parser_bool, parser_result
        elif command_terms[0] == 'next':
            if command_terms_len == 1:
                #播放下一首
                service_bool,msg = player.next()
                parser_bool = True
                parser_result = self.__parser_result_helper(parser_bool, msg, command)
                return parser_bool, parser_result
            else:
                #存在参数， 命令格式有误， 解析失败
                parser_bool = False
                parser_result = self.__parser_result_helper(parser_bool, "参数过多，不符合命令规范" % (command))
                return parser_bool, parser_result
        elif command_terms[0] == 'up':
            if command_terms_len == 1:
                #没参数默认提高一个音量
                service_bool, msg = player.up()
                parser_bool = True
                parser_result = self.__parser_result_helper(parser_bool, msg, command)
                return parser_bool, parser_result
            elif command_terms_len == 2:
                if command_terms[1].isdigit() == False:
                    #输入不是纯数字，浮点数或者有字符
                    parser_bool = False
                    parser_result = self.__parser_result_helper(parser_bool, "输入不符合规范", command)
                    return parser_bool, parser_result
                step = eval(command_terms[1])
                #调用服务层服务 设置音量
                service_bool, msg = player.up(step)
                parser_bool = True
                parser_result = self.__parser_result_helper(parser_bool, msg, command)
                return parser_bool, parser_result
            else:
                #参数过多，命令不符合规范
                parser_bool = False
                parser_result = self.__parser_result_helper(parser_bool, "参数过多，不符合命令规范" % (command))
                return parser_bool, parser_result
        elif command_terms[0] == 'down':
            if command_terms_len == 1:
                # 没参数默认提高一个音量
                service_bool, msg = player.down()
                parser_bool = True
                parser_result = self.__parser_result_helper(parser_bool, msg, command)
                return parser_bool, parser_result
            elif command_terms_len == 2:
                if command_terms[1].isdigit() == False:
                    # 输入不是纯数字，浮点数或者有字符
                    parser_bool = False
                    parser_result = self.__parser_result_helper(parser_bool, "输入不符合规范", command)
                    return parser_bool, parser_result
                step = eval(command_terms[1])
                # 调用服务层服务 设置音量
                service_bool, msg = player.down(step)
                parser_bool = True
                parser_result = self.__parser_result_helper(parser_bool, msg, command)
                return parser_bool, parser_result
            else:
                # 参数过多，命令不符合规范
                parser_bool = False
                parser_result = self.__parser_result_helper(parser_bool, "参数过多，不符合命令规范" % (command))
                return parser_bool, parser_result
        elif command_terms[0] == "pause":
            if command_terms_len == 1:
                #命令格式正确，暂停正在播放的音乐
                service_bool, msg = player.pause()
                parser_bool = True
                parser_result = self.__parser_result_helper(parser_bool, msg, command)
                return parser_bool, parser_result
            else:
                #参数过多，命令格式不符合规范
                parser_bool = False
                parser_result = self.__parser_result_helper(parser_bool, "参数过多，不符合命令规范" % (command))
                return parser_bool, parser_result
        elif command_terms[0] == "stop":
            if command_terms_len == 1:
                #命令格式正确，停止正在播放的音乐
                service_bool, msg = player.stop()
                parser_bool = True
                parser_result = self.__parser_result_helper(parser_bool, msg, command)
                return parser_bool, parser_result
            else:
                #参数过多，命令格式不符合规范
                parser_bool = False
                parser_result = self.__parser_result_helper(parser_bool, "参数过多，不符合命令规范" % (command))
                return parser_bool, parser_result
        elif command_terms[0] == "lyric":
            if command_terms_len == 1:
                #命令格式正确，显示歌词
                parser_result = "PARSER SUCCESS %s" % (command)
                parser_bool = True
                return parser_bool, parser_result
            else:
                #参数过多，命令格式不符合规范
                parser_result = "PARSER ERROR: %s" % (command)
                parser_bool = False
                return parser_bool, parser_result
        elif command_terms[0] == "mode":
            if command_terms_len == 1:
                # mode顺序向下切换一个
                service_bool, msg = player.mode()
                parser_bool = True
                parser_result = self.__parser_result_helper(parser_bool, msg, command)
                return parser_bool, parser_result
            elif command_terms_len == 2:
                # 切换到指定模式
                service_bool, msg = player.mode(command_terms[1])
                parser_bool = True
                parser_result = self.__parser_result_helper(parser_bool, msg, command)
                return parser_bool, parser_result
            else:
                # 参数过多，命令格式不符合规范
                parser_bool = False
                parser_result = self.__parser_result_helper(parser_bool, "参数过多，不符合命令规范" % (command))
                return parser_bool, parser_result
        elif command_terms[0] == "list":
            if command_terms_len == 1:
                #命令格式正确，显示列表往下十首
                service_bool, msg, names = player.list()
                parser_bool = True
                parser_result = self.__parser_result_helper(parser_bool, msg, command)
                id = 1
                for name in names:
                    parser_result += "%d: %s\n" % (id, name)
                    id += 1
                return parser_bool, parser_result
            elif command_terms_len == 2:
                #命令格式正确，显示列表往下num首
                if command_terms[1].isdigit() == False:
                    #输入不是纯数字，浮点数或者有字符
                    parser_bool = False
                    parser_result = self.__parser_result_helper(parser_bool, "输入不符合规范", command)
                    return parser_bool, parser_result
                num = eval(command_terms[1])
                service_bool, msg, names = player.list(num)
                parser_bool = True
                parser_result = self.__parser_result_helper(parser_bool, msg, command)
                id = 1
                for name in names:
                    parser_result += "%d: %s\n" % (id, name)
                    id += 1
                return parser_bool, parser_result
            else:
                # 参数过多，命令格式不符合规范
                parser_bool = False
                parser_result = self.__parser_result_helper(parser_bool, "参数过多，不符合命令规范" % (command))
                return parser_bool, parser_result
        elif command_terms[0] == "delete":
            if command_terms_len == 1:
                #删除当前正在播放的歌曲
                parser_result = "PARSER SUCCESS: %s" % (command)
                parser_bool = True
                return parser_bool, parser_result
            elif command_terms_len == 2:
                #删除指定了歌名的歌曲
                parser_result = "PARSER SUCCESS: %s" % (command)
                parser_bool = True
                return parser_bool, parser_result
            else:
                #命令格式不符合规范
                parser_result = "PARSER ERROR: %s" % (command)
                parser_bool = False
                return parser_bool, parser_result
        elif command_terms[0] == "pwd":
            if command_terms_len == 1:
                #显示当前目录
                service_bool, msg = player.pwd()
                parser_bool = True
                parser_result = self.__parser_result_helper(parser_bool, msg, command)
                return parser_bool, parser_result
            # elif command_terms_len == 2:
            #     #显示歌名对应的歌曲所在的目录
            #     parser_result = "PARSER SUCCESS: %s" % (command)
            #     parser_bool = True
            #     return parser_bool, parser_result
            else:
                # 命令格式不符合规范
                parser_bool = False
                parser_result = self.__parser_result_helper(parser_bool, "参数过多，不符合命令规范" % (command))
                return parser_bool, parser_result
        elif command_terms[0] == "cd":
            if command_terms_len == 2:
                #切换到指定目录
                service_bool, msg = player.cd(command_terms[1])
                parser_bool = True
                parser_result = self.__parser_result_helper(parser_bool, msg, command)
                return parser_bool, parser_result
            else:
                # 命令格式不符合规范
                parser_bool = False
                parser_result = self.__parser_result_helper(parser_bool, "参数过多，不符合命令规范" % (command))
                return parser_bool, parser_result
        elif command_terms[0] == "quit":
            if command_terms_len == 1:
                #退出音乐播放器
                parser_result = "PARSER SUCCESS: %s" % (command)
                parser_bool = True
                return parser_bool, parser_result
            else:
                # 命令格式不符合规范
                parser_result = "PARSER ERROR: %s" % (command)
                parser_bool = False
                return parser_bool, parser_result
        elif command_terms[0] == "load":
            if command_terms_len == 1:
                #在当前目录加载所有mp3音乐文件
                service_bool, msg = player.load()
                parser_bool = True
                parser_msg = self.__parser_result_helper(parser_bool, msg, command)
                return parser_bool, parser_msg
            elif command_terms_len == 2:
                service_bool, msg = player.load(command_terms[1])
                parser_bool = True
                parser_msg = self.__parser_result_helper(parser_bool, msg, command)
                return parser_bool, parser_msg
            else:
                parser_bool = False
                parser_msg = self.__parser_result_helper(parser_bool, "参数过多， 不符合命令规范", command)
                return parser_bool, parser_msg
        elif command_terms[0] == "analyze":
            if command_terms_len == 2:
                #进行文本分析
                service_bool, msg = player.analyze(command_terms[1])
                parser_bool = True
                parser_msg = self.__parser_result_helper(parser_bool, msg, command)
                return parser_bool, parser_msg
            else:
                parser_bool = False
                parser_msg = self.__parser_result_helper(parser_bool, "参数不符合命令规范", command)
                return parser_bool, parser_msg
        elif command_terms[0] == "status":
            if command_terms_len == 1:
                #播放器模式的切换
                service_bool, msg = player.status()
                parser_bool = True
                parser_msg = self.__parser_result_helper(parser_bool, msg, command)
                return parser_bool, parser_msg
            elif command_terms_len == 2:
                service_bool, msg = player.analyze(command_terms[1])
                parser_bool = True
                parser_msg = self.__parser_result_helper(parser_bool, msg, command)
                return parser_bool, parser_msg
            else:
                parser_bool = False
                parser_msg = self.__parser_result_helper(parser_bool, "参数过多，不符合命令规范", command)
                return parser_bool, parser_msg
        else:
            #不存在的命令
            parser_msg = "PARSER ERROR: %s" % (command)
            parser_bool = False
            return parser_bool, parser_msg

    def __parser_result_helper(self, parser_bool, service_msg, command):
        '''
        :param parser_bool: 解析层解析结果（bool值的结果为累积结果，来源解析层及以下）
        :param service_msg: 服务层的信息，将在该函数中封装后返回
        :param command: parser解析的命令
        :return: parser_msg String类型，封装后的解析结果
        '''
        if parser_bool:
            parser_msg = "PARSER SUCCESS: %s\n" % (command) + service_msg
        else:
            parser_msg = "PARSER ERROR: %s\n" % (command) + service_msg
        return parser_msg


if __name__ == '__main__':
    singeton = Parser()
    singeton2 = Parser()
    singeton.parser_command("play")
    print(id(singeton))
    print(id(singeton2))