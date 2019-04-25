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

import time
import abc
from music_player import ListItem

class Abstract_PlayList(object):
    '''
    播放列表的抽象基类
    包含了抽象属性和方法
    '''
    __metaclass__ = abc.ABCMeta

    @property
    @abc.abstractmethod
    def list_container(self):
        return self._list_container

    @list_container.setter
    def list_container(self, list_container):
        self._list_container = list_container

    @property
    @abc.abstractmethod
    def current_item(self):
        return self._current_item

    @current_item.setter
    def current_item(self, current_item):
        self._current_item = current_item

    @property
    @abc.abstractmethod
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        self._create_time = create_time

    @property
    @abc.abstractmethod
    def length(self):
        return len(self.list_container)


class PlayList(Abstract_PlayList):
    '''
    该类为普通的播放列表类
    list_container: 包含列表项的容器
    current_Item: 当前播放的索引
    create_time: 创建时间
    '''
    def __init__(self, list_container, current_item=0, create_time=""):
        self.list_container = list_container
        self.current_item = current_item
        if create_time == "":
            self.create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        else:
            self.create_time = create_time

    @property
    def length(self):
        return len(self.list_container)

    def append_item(self, item):
        '''
        该函数用于向播放列表中添加歌曲
        歌曲被封装成item的形式
        :param item: 歌曲被封装成item格式
        :return: msg:封装好的信息
                 service_bool: 该层执行结果
        '''
        if ~isinstance(item, ListItem.ListItem):
            service_bool = False
            msg = self.service_result_helper(service_bool, "添加歌曲类型不符合规范")
            return service_bool, msg
        self.list_container.append(item)
        service_bool = True
        msg = self.service_result_helper(service_bool, "添加歌曲成功")
        return service_bool, msg

    def service_result_helper(self, service_bool, msg):
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