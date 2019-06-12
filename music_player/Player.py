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
import sys
from music_player.PlayerList import  PlayList
from enum import Enum, unique
from mutagen.mp3 import MP3
from music_player.ListItem import ListItem
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import QUrl
from analyze.Analyze import Analyze

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
    __mode_name_table = {QMediaPlaylist.CurrentItemOnce: "单曲播放",
                        QMediaPlaylist.CurrentItemInLoop: "单曲循环",
                        QMediaPlaylist.Sequential: "顺序播放",
                        QMediaPlaylist.Loop: "循环播放",
                        QMediaPlaylist.Random: "随机播放"}
    __mode_table = {"once": QMediaPlaylist.CurrentItemOnce,
                    "single_loop": QMediaPlaylist.CurrentItemInLoop,
                    "sequential": QMediaPlaylist.Sequential,
                    "loop": QMediaPlaylist.Loop,
                    "random": QMediaPlaylist.Random}
    #__status = Status.none
    __status = Status.Music
    __current_player = QMediaPlayer()
    __current_playerList = None
    __happy_playerList = None
    __sad_playerList = None
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
        if self.__status != Status.Music:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "处于阅读模式下，该命令无效")
            return service_bool, msg
        if self.__current_playerList == None or new_list == True:
            self.__current_playerList = QMediaPlaylist()
        if dir == "":
            abs_dir = os.getcwd()
        else:
            abs_dir = os.path.abspath(dir)
        count = 0
        for root, dirs, files in os.walk(abs_dir):
            if root != abs_dir and os.path.isdir(root):
                continue
            for file in files:
                if os.path.splitext(file)[1] == '.mp3':
                    print(os.path.join(root, file))
                    item = QMediaContent(QUrl.fromLocalFile(os.path.join(root, file)))
                    self.__current_playerList.addMedia(item)
                    count += 1
        service_bool = True
        msg = self.__service_result_helper(service_bool, "加载音乐成功，共加载音乐%d首" % (count))
        return service_bool, msg

    def play(self, name=""):
        '''
        该函数用于播放指定音乐
        :param name: 默认值为空时，播放当前播放列表的当前音乐
        否则播放指定名字的音乐，若该名字音乐不存在，则不进行播放
        :return: service_bool: 服务层执行结果
        msg: 服务层执行结果信息
        '''
        if self.__status != Status.Music:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "处于阅读模式下，该命令无效")
            return service_bool, msg
        if self.__current_playerList == None:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "未载入音乐，请先载入音乐")
            return service_bool, msg
        if name != "":
            exist = self.__contains_item(name)
            if  exist == -1:
                service_bool = False
                msg = self.__service_result_helper(service_bool, "播放列表中不存在该音乐")
                return service_bool, msg
            if self.__current_player.playlist() != self.__current_playerList:
                self.__current_player.setPlaylist(self.__current_playerList)
            #self.__current_player.setVolume(50)
            self.__current_playerList.setCurrentIndex(exist)
            self.__current_player.play()
            service_bool = True
            msg = self.__service_result_helper(service_bool, "播放音乐: %s" % (name))
            return service_bool, msg
        else:
            if self.__current_player.playlist() != self.__current_playerList:
                self.__current_player.setPlaylist(self.__current_playerList)
            #self.__current_player.setVolume(50)
            #self.__current_playerList.setCurrentIndex(0)
            self.__current_player.play()
            service_bool = True
            idx = self.__current_playerList.currentIndex()
            name = self.__current_playerList.media(idx).canonicalUrl().fileName()
            msg = self.__service_result_helper(service_bool, "播放音乐: %s" % (name))
            return service_bool, msg

    def next(self, step=1):
        '''
        该函数用于播放下一首或下n首歌曲
        :param step: 表示要播放距离，默认为一，播放下一首
        :return: service_bool: 服务层执行结果
        msg: 服务层执行信息
        '''
        if self.__status != Status.Music:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "处于阅读模式下，该命令无效")
            return service_bool, msg
        if self.__current_playerList == None:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "未载入音乐，请先载入音乐")
            return service_bool, msg
        if self.__current_playerList != self.__current_player.playlist():
            self.__current_player.setPlaylist(self.__current_playerList)

        current_idx_old = self.__current_playerList.currentIndex()
        if (self.__current_playerList.playbackMode() == QMediaPlaylist.Sequential and current_idx_old == -1) or (
                self.__current_playerList.playbackMode()== QMediaPlaylist.CurrentItemInLoop and current_idx_old == -1):
            service_bool = False
            msg = self.__service_result_helper(service_bool, "播放列表中不存在下一首音乐")
            return service_bool, msg
        self.__current_playerList.next()
        current_idx_new = self.__current_playerList.currentIndex()
        if (self.__current_playerList.playbackMode() == QMediaPlaylist.Sequential and current_idx_old == -1) or (
                self.__current_playerList.playbackMode()== QMediaPlaylist.CurrentItemInLoop and current_idx_old == -1):
            service_bool = False
            msg = self.__service_result_helper(service_bool, "播放列表中不存在下一首音乐")
            return service_bool, msg

        service_bool = True
        idx = self.__current_playerList.currentIndex()
        name = self.__current_playerList.media(idx).canonicalUrl().fileName()
        msg = self.__service_result_helper(service_bool, "成功播放下一首歌曲：%s" % (name))
        return service_bool, msg

    def previous(self, step=1):
        '''
        该函数用于播放上一首或上n首歌曲
        :param step: 表示要播放距离，默认为一，播放上一首
        :return: service_bool: 服务层执行结果
        msg: 服务层执行信息
        '''
        if self.__status != Status.Music:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "处于阅读模式下，该命令无效")
            return service_bool, msg
        if self.__current_playerList == None:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "未载入音乐，请先载入音乐")
            return service_bool, msg
        if self.__current_playerList != self.__current_player.playlist():
            self.__current_player.setPlaylist(self.__current_playerList)

        current_idx_old = self.__current_playerList.currentIndex()
        if (self.__current_playerList.playbackMode() == QMediaPlaylist.Sequential and current_idx_old == -1) or (
                self.__current_playerList.playbackMode()== QMediaPlaylist.CurrentItemInLoop and current_idx_old == -1):
            service_bool = False
            msg = self.__service_result_helper(service_bool, "播放列表中不存在上一首音乐")
            return service_bool, msg
        self.__current_playerList.previous()
        print(current_idx_old)
        current_idx_new = self.__current_playerList.currentIndex()
        if (self.__current_playerList.playbackMode() == QMediaPlaylist.Sequential and current_idx_old == -1) or (
                self.__current_playerList.playbackMode()== QMediaPlaylist.CurrentItemInLoop and current_idx_old == -1):
            service_bool = False
            msg = self.__service_result_helper(service_bool, "播放列表中不存在上一首音乐")
            return service_bool, msg

        service_bool = True
        name = self.__current_playerList.media(current_idx_new).canonicalUrl().fileName()
        msg = self.__service_result_helper(service_bool, "成功播放上一首歌曲：%s" % (name))
        return service_bool, msg

    def up(self, step=1):
        '''
        该函数用于提高音量，step表示提高音量提高值
        :param step:
        :return:
        '''
        if self.__status != Status.Music:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "处于阅读模式下，该命令无效")
            return service_bool, msg
        if self.__current_playerList == None:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "未载入音乐，请先载入音乐")
            return service_bool, msg
        if step > 100 or step < 0:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "输入的音量值不符合规范")
            return service_bool, msg
        if self.__current_player.volume() + step > 100:
            self.__current_player.setVolume(100)
            service_bool = True
            msg = self.__service_result_helper(service_bool, "音量值已经达到最大")
            return service_bool, msg
        self.__current_player.setVolume(self.__current_player.volume() + step)
        service_bool = True
        msg = self.__service_result_helper(service_bool, "音量调整为：%d" % (self.__current_player.volume()))
        return service_bool, msg

    def down(self, step=1):
        '''
        该函数用于降低音量，step表示提高音量提高值
        :param step: 表示降低的幅度
        :return:
        '''
        if self.__status != Status.Music:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "处于阅读模式下，该命令无效")
            return service_bool, msg
        if self.__current_playerList == None:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "未载入音乐，请先载入音乐")
            return service_bool, msg
        if step > 100 or step < 0:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "输入的音量值不符合规范")
            return service_bool, msg
        if self.__current_player.volume() - step < 0:
            self.__current_player.setVolume(0)
            service_bool = True
            msg = self.__service_result_helper(service_bool, "音量值已经达到最大")
            return service_bool, msg
        self.__current_player.setVolume(self.__current_player.volume() - step)
        service_bool = True
        msg = self.__service_result_helper(service_bool, "音量调整为：%d" % (self.__current_player.volume()))
        return service_bool, msg

    def pause(self):
        '''
        该函数用于暂停正在播放的音乐
        :return:
        '''
        if self.__status != Status.Music:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "处于阅读模式下，该命令无效")
            return service_bool, msg
        self.__current_player.pause()
        service_bool = True
        idx = self.__current_playerList.currentIndex()
        name = self.__current_playerList.media(idx).canonicalUrl().fileName()
        msg = self.__service_result_helper(service_bool, "暂停播放音乐%s" % (name))
        return service_bool, msg

    def stop(self):
        '''
        该函数用于停止正在播放的音乐
        :return: service_bool: 表示执行的结果
        msg: 执行结果信息
        '''
        if self.__status != Status.Music:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "处于阅读模式下，该命令无效")
            return service_bool, msg
        self.__current_player.stop()
        service_bool = True
        idx = self.__current_playerList.currentIndex()
        name = self.__current_playerList.media(idx).canonicalUrl().fileName()
        msg = self.__service_result_helper(service_bool, "停止播放音乐%s" % (name))
        return service_bool, msg

    def mode(self, m=""):
        '''
        该函数用于切换播放模式
        :param m:  表示要切换的播放模式，若为空串，则为往下的一个模式
        :return:
        '''
        if self.__status != Status.Music:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "处于阅读模式下，该命令无效")
            return service_bool, msg
        if m == "":
            self.__current_playerList.setPlaybackMode((1 + self.__current_playerList.playbackMode()) % 5)
            service_bool = True
            msg = self.__service_result_helper(service_bool, "切换音乐播放模式为: %s" % (self.__mode_name_table[
                self.__current_playerList.playbackMode()]))
            return service_bool, msg
        else:
            if m in self.__mode_table:
                service_bool = False
                msg = self.__service_result_helper(service_bool, "模式参数输入不正确")
                return service_bool, msg
            mod = self.__mode_table[m]
            self.__current_playerList.setPlaybackMode(mod)
            service_bool = True
            msg = self.__service_result_helper(service_bool, "切换音乐播放模式为: %s" % (self.__mode_name_table[mod]))
            return service_bool, msg

    def list(self, num=10):
        '''
        该函数用于显示当前播放列表
        :param num: 表示显示多少首歌信息
        :return: service_bool: 服务层执行结果
        msg: 服务层执行信息
        names: list类型，播放列表中从当前开始的下num首歌名
        '''
        if self.__status != Status.Music:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "处于阅读模式下，该命令无效")
            names = []
            return service_bool, msg, names
        if self.__current_playerList == None:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "无播放列表，请先载入音乐")
            names = []
            return service_bool, msg, names
        len = self.__current_playerList.mediaCount()
        idx = self.__current_playerList.currentIndex()
        it = 0
        names = []
        while idx < len and it < num:
            if idx == -1:
                idx += 1
                continue
            name = self.__current_playerList.media(idx).canonicalUrl().fileName()
            names.append(name)
            it += 1
            idx += 1
        service_bool = True
        msg = self.__service_result_helper(service_bool, "当前%d首歌为：" % (num))
        return service_bool, msg, names

    def pwd(self):
        '''
        显示音乐播放器当前的工作目录
        :return: service_bool: 服务层执行结果
        msg: 服务层执行信息
        '''
        abs_dir = os.getcwd()
        service_bool = True
        msg = self.__service_result_helper(service_bool, "当前的工作目录为: %s" % (abs_dir))
        return service_bool, msg

    def cd(self, path):
        '''
        切换音乐播放器的当前工作目录
        :param path: 切换的目录
        :return: service_bool: 服务层执行结果
        msg: 服务层执行信息
        '''
        abs_dir = os.path.abspath(path)
        os.chdir(abs_dir)
        service_bool = True
        msg = self.__service_result_helper(service_bool, "当前的工作目录切换为：%s" % (abs_dir))
        return service_bool, msg

    def __contains_item(self, name):
        '''
        通过名字确定歌曲是否在播放列表中
        :param name: 歌曲名
        :return: int类型，-1表示item不存在
        '''
        if self.__current_playerList == None:
            return False
        len = self.__current_playerList.mediaCount()
        for L in range(len):
            url = self.__current_playerList.media(L).canonicalUrl()
            filename = url.fileName().split('.')[0].strip()
            if filename == name:
                return  L
        return -1

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

    def analyze(self, filepath):
        '''
        根据文本分析结果播放相应的开心或悲伤的音乐
        :param emotion:  positive_prob 浮点数表示积极所占的可能性
        text: 文本内容
        :return: service_bool: 服务层执行结果
        msg: 服务层执行信息
        '''
        if self.__status != Status.Read:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "处于播放模式下，该命令无效")
            return service_bool, msg

        abs_dir, temp_file_name = os.path.split(os.path.abspath(sys.argv[0]))
        happy_dir = abs_dir + "\\happy"
        print(happy_dir)
        sad_dir = abs_dir + "\\sad"
        print(sad_dir)
        if not os.path.isdir(happy_dir):
            service_bool = False
            msg = self.__service_result_helper(service_bool, "happy文件夹不存在，请在目录下创建")
            return service_bool, msg
        if not os.listdir(happy_dir):
            service_bool = False
            msg = self.__service_result_helper(service_bool, "happy文件夹中不存在音乐文件")
            return service_bool, msg
        if not os.path.isdir(sad_dir):
            service_bool = False
            msg = self.__service_result_helper(service_bool, "sad文件夹不存在，请在目录下创建")
            return service_bool, msg
        if not os.listdir(sad_dir):
            service_bool = False
            msg = self.__service_result_helper(service_bool, "sad文件夹中不存在音乐文件")
            return service_bool, msg

        self.__happy_playerList = QMediaPlaylist()
        self.__sad_playerList = QMediaPlaylist()
        count = 0
        for root, dirs, files in os.walk(happy_dir):
            for file in files:
                if os.path.splitext(file)[1] == '.mp3':
                    print(os.path.join(root, file))
                    item = QMediaContent(QUrl.fromLocalFile(os.path.join(root, file)))
                    self.__happy_playerList.addMedia(item)
                    count += 1
        if count == 0:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "happy文件夹中不存在音乐文件")
            return service_bool, msg
        count = 0
        for root, dirs, files in os.walk(sad_dir):
            for file in files:
                if os.path.splitext(file)[1] == '.mp3':
                    print(os.path.join(root, file))
                    item = QMediaContent(QUrl.fromLocalFile(os.path.join(root, file)))
                    self.__sad_playerList.addMedia(item)
                    count += 1
        if count == 0:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "sad文件夹中不存在音乐文件")
            return service_bool, msg

        abs_filepath = os.path.abspath(filepath)
        with open(abs_filepath, 'r') as f:
            text = f.read()
        analyze = Analyze()
        emotion = analyze.sentiment_classify(text)
        print(emotion)
        if emotion > 0.5:
            self.__happy_playerList.setPlaybackMode(QMediaPlaylist.Random)
            self.__current_player.setPlaylist(self.__happy_playerList)
            self.__current_player.play()
        else:
            self.__sad_playerList.setPlaybackMode(QMediaPlaylist.Random)
            self.__current_player.setPlaylist(self.__sad_playerList)
            self.__current_player.play()
        service_bool = True
        msg = self.__service_result_helper(service_bool, "分析成功，该文章积极倾向为%f\n文本内容:\n%s" % (emotion, text))
        return service_bool, msg

    def status(self, s=""):
        '''
        :param s: 用于指明切换到的模式的显式参数
        :return: service_bool 服务层执行结果
        msg 服务层执行信息
        '''
        if s == "":
            if self.__status == Status.Music:
                self.__status = Status.Read
                service_bool = True
                msg = self.__service_result_helper(service_bool, "播放器切换为文本分析模式")
                return service_bool, msg
            else:
                self.__status = Status.Music
                self.__current_player.setPlaylist(self.__current_playerList)
                service_bool = True
                msg = self.__service_result_helper(service_bool, "播放器切换为音乐播放模式")
                return service_bool, msg
        elif s in ['read', 'music']:
            if s == 'read':
                self.__status = Status.Read
                service_bool = True
                msg = self.__service_result_helper(service_bool, "播放器切换为文本分析模式")
                return service_bool, msg
            else:
                self.__status = Status.Music
                self.__current_player.setPlaylist(self.__current_playerList)
                service_bool = True
                msg = self.__service_result_helper(service_bool, "播放器切换为音乐播放模式")
                return service_bool, msg
        else:
            service_bool = False
            msg = self.__service_result_helper(service_bool, "参数不规范")
            return service_bool, msg
