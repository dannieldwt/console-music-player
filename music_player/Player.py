#!/usr/bin/env python
# encoding: utf-8
'''
@author: Danniel
@license: (C) Copyright
@contact: 1085837135@qq.com
@software: PyCharm
@file: Player.py
@time: 2019-04-19 19:54
@desc:
该文件包含了对于Player类的定义，是服务层核心类
采用单例模式，提供了播放音乐，暂停音乐等接口，
播放音乐采用pyGame库
'''

import pygame
import os
from music_player.PlayerList import  PlayList
from enum import Enum, unique
from mutagen.mp3 import MP3
from music_player.ListItem import ListItem

@unique
class Mode(Enum):
    '''
    枚举类定义，包含了播放器支持的音乐播放模式
    '''
    none = 0
    Sequential = 1
    Loop = 2
    Random = 3
    Single = 4

@unique
class Status(Enum):
    '''
    枚举类定义，包含了播放器所处的模式，阅读还是音乐播放模式
    '''
    none = 0
    Read = 1
    Music = 2

class Player(object):
    '''
    服务层的核心类，播放器，采用单例模式。
    使用PyGame进行音乐播放， 向上层提供音乐播放接口
    '''
    __mode = Mode.none
    __status = Status.none
    __volume = 50
    __current_playerList = None
    __instance = None

    def __new__(cls, *args, **kwargs):
        if Player.__instance == None:
            Player.__instance = object.__new__(Player)
        return Player.__instance

    def load(self, dir="", new_list=False):
        '''
        该函数用于加载某个目录下的音乐
        :param dir: 目录名，可以是绝对路径也能是相对路径，均被处理为绝对路径
        若目录名为空，则默认为当前目录。
        :param new_list: 表示是否加载音乐后，同时产生一个新的播放列表
        默认为False，将在原播放列表后插入新载入的歌曲
        :return: service-bool: 服务层执行结果
        msg: 服务层执行结果信息
        '''
        if self.__current_playerList == None or new_list == False:
            self.__current_playerList = PlayList([])
        if dir == "":
            abs_dir = os.getcwd()
        else:
            abs_dir = os.path.abspath(dir)
        count = 0
        for root, dirs, files in os.walk(abs_dir):
            for file in files:
                if os.path.splitext(file)[1] == '.mp3':
                    item = ListItem(os.path.join(root, file))
                    self.__current_playerList.append_item(item)
                    count += 1
        service_bool = True
        msg = self.__service_result_helper(service_bool, "加载音乐成功，共加载音乐%d首" % (count))
        return service_bool, msg


    def __service_result_helper(self, service_bool, msg):
        '''
        :param service_bool: 服务层服务执行结果
        :param msg: 服务层执行成功与否的信息
        :return: 封装好的信息
        '''
        if service_bool:
            msg = "SERVICE SUCCESS: %s\n" % (msg)
        else:
            msg = "SERVICE ERROR: %s\n" % (msg)
        return msg