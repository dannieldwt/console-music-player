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

import logging
import pygame
from enum import Enum, unique
from mutagen.mp3 import MP3

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='console-music-player.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

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
    __instance = None

    def __new__(cls, *args, **kwargs):
        if Player.__instance == None:
            Player.__instance = object.__new__(Player)
        return Player.__instance

