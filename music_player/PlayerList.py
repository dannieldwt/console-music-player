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

class PlayList(Abstract_PlayList):
    '''
    该类为普通的播放列表类
    list_container: 包含列表项的容器
    current_Item: 当前播放的索引
    create_time: 创建时间
    '''
    def __init__(self, list_container, current_item=1, create_time=""):
        self.__list_container = list_container
        self.__current_Item = current_item - 1
        if create_time == "":
            self.create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        else:
            self.create_time = create_time

    @property
    def list_container(self):
        return self.list_container

    @list_container.setter
    def list_container(self, list_container):
        self.list_container = list_container

    @property
    def current_Item(self):
        return self.current_Item

    @current_Item.setter
    def current_Item(self, current_Item):
        self.current_Item = current_Item

    @property
    def create_time(self):
        return self.create_time

    @create_time.setter
    def create_time(self, create_time):
        self.create_time = create_time
