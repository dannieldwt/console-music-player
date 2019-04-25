#!/usr/bin/env python
# encoding: utf-8
'''
@author: Danniel
@license: (C) Copyright
@contact: 1085837135@qq.com
@software: PyCharm
@file: test.py
@time: 2019-04-13 18:29
@desc:
该文件是在项目创立时候（可能以后维护更新的时候仍会使用）的
测试文件，用于测试每个模块的运行状态
'''

import logging
import pygame
import time
import os
import threading

from mutagen.mp3 import MP3

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='console-music-player.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

file="city of stars.mp3"
#pygame.mixer.init()
#track = pygame.mixer.music.load(file)
#pygame.mixer.music.play(1)
#pygame.mixer.music.stop()
#audio = MP3(file)
#time_mp3 = audio.info.length
#time.sleep(time_mp3)


def test_play(file):
    print("测试")
    audio = MP3(file)
    time_mp3 = audio.info.length
    pygame.mixer.init()
    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play(1)
    time.sleep(time_mp3)


# t= threading.Thread(target=test_play,args=(file,))
# #t.setDaemon(True)
# t.start()#开启线程

path = "D:\console-music-player\console-music-player\music_player"
newpath = os.path.abspath(path)
print(newpath)

