#!/usr/bin/env python
# encoding: utf-8
'''
@author: Danniel
@license: (C) Copyright
@contact: 1085837135@qq.com
@software: PyCharm
@file: ListItem.py
@time: 2019-04-19 20:30
@desc:
该文件包含播放列表列表项类，
每一项表示一首歌曲
'''

import logging
import time
from music_player.Song import Song

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='console-music-player.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

class ListItem(object):
    '''
    该类为播放列表列表项类
    一项对应一首歌曲
    '''
    __count = 0

    def __init__(self, filepath, create_time=""):
        self.__ID = self.__count
        self.__count += 1
        self.__song = Song(filepath)
        if create_time != "":
            self.__create_time = create_time
        else:
            self.__create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID):
        self.__ID = ID

    @property
    def song(self):
        return self.__song

    @song.setter
    def song(self, song):
        self.__song = song

    @property
    def create_time(self):
        return self.__create_time

    @create_time.setter
    def create_time(self, create_time):
        self.create_time = create_time

if __name__ == '__main__':
    song = Song(10023, "D:\console-music-player\console-music-player\city of stars.mp3")
    item = ListItem(10283, song)
    print(item.song.name)
    print(item.ID)
    print(item.create_time)