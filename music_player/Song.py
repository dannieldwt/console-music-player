#!/usr/bin/env python
# encoding: utf-8
'''
@author: Danniel
@license: (C) Copyright
@contact: 1085837135@qq.com
@software: PyCharm
@file: Song.py
@time: 2019-04-19 20:15
@desc:
该类是关于歌曲的定义
包含了歌曲的属性和接口
'''

import logging
import os

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='console-music-player.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

class Song(object):
    '''
    歌曲类，包含了歌曲的基本属性以及接口
    '''
    __count = 0

    def __init__(self, filepath):
        self.__ID = self.__count
        self.__count += 1
        self.__filepath = filepath
        self.__name = os.path.basename(filepath)
        self.__length = 0
        self.__duration = 0
        self.__singer = ""
        self.__album = ""

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID):
        self.__ID = ID

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def filepath(self):
        return self.__filepath

    @filepath.setter
    def filepath(self, filepath):
        self.__filepath = filepath


if __name__ == '__main__':
    song1 = Song(1001, "D:\console-music-player\console-music-player\city of stars.mp3")
    print(song1.name)
    print(song1.ID)
    print(song1.filepath)

