#!/usr/bin/env python
# encoding: utf-8
'''
@author: 10858
@license: (C) Copyright
@contact: xxx@qq.com
@software: PyCharm
@file: Analyze.py
@time: 2019-06-11 21:26
@desc:
该类对情感分析方法进行封装
情感分析目前暂时采用百度AI的情感分析API
'''

import urllib, sys
import json
import ssl

class Analyze(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if Analyze.__instance == None:
            Analyze.__instance = object.__new__(Analyze)
            host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=rBH9rnBsIXwCVUPMS2MpbOMN&client_secret=PjMNQHBxaRDrncOozUYPxPlhmFuqmCTn'
            request = urllib.request.Request(host)
            request.add_header('Content-Type', 'application/json; charset=UTF-8')
            response = urllib.request.urlopen(request)
            content = response.read().decode('utf-8')
            rdata = json.loads(content)
            print(rdata)
            Analyze.__instance.AT = rdata['access_token']
        return Analyze.__instance

    def __get_access_token(self):
        """
        获取百度AI平台的Access Token
        """
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=rBH9rnBsIXwCVUPMS2MpbOMN&client_secret=PjMNQHBxaRDrncOozUYPxPlhmFuqmCTn'
        request = urllib.request.Request(host)
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        rdata = json.loads(content)
        return rdata['access_token']

    def sentiment_classify(self,text):
        """
        获取文本分析的结果
        该函数调用百度AI的API
        参数为text: 文本分析的字符串
        返回值为positive_prob: 积极性占比
        """
        raw = {"text": "内容"}
        raw['text'] = text
        data = json.dumps(raw).encode('utf-8')
        host = "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=UTF-8&access_token=" + Analyze.__instance.AT
        request = urllib.request.Request(url=host, data=data)
        request.add_header('Content-Type', 'application/json')
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        rdata = json.loads(content)
        return rdata['items'][0]['positive_prob']

if __name__ == '__main__':
    singeton = Analyze()
    print(singeton.AT)
    print(singeton.sentiment_classify("苹果是一间伟大的公司"))