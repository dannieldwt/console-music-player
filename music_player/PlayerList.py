#!/usr/bin/env python
# encoding: utf-8
'''
@author: 10858
@license: (C) Copyright
@contact: xxx@qq.com
@software: PyCharm
@file: PlayerList.py
@time: 2019-04-19 22:08
@desc:
该文件包含了播放列表抽象基类
普通播放列表，收藏列表，拉黑列表的定义
'''

import logging
import time
import abc

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='console-music-player.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

class Abstract_PlayList(object):
    '''
    播放列表的抽象基类
    包含了抽象属性和方法
    '''
    __metaclass__ = abc.ABCMeta

    @property
    @abc.abstractmethod
    def list_container(self):
        return self.list_container

    @list_container.setter
    def list_container(self, list_container):
        self.list_container = list_container

    @property
    @abc.abstractmethod
    def current_Item(self):
        return self.__current_Item

    @current_Item.setter
    def current_Item(self, current_Item):
        self.current_Item = current_Item

    @property
    @abc.abstractmethod
    def create_time(self):
        return self.create_time

    @create_time.setter
    def create_time(self, create_time):
        self.create_time = create_time

    @abc.abstractmethod
    def play(self):
        pass

