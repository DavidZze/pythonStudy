#! /usr/bin/python
# -*- coding=utf-8 -*-


import urllib,urllib2
import json


"""
http client： 
用于发送http的请求（get ,post ）
"""
class HttpClientDemo:


    """
    构造器
    """
    def __init__(self, method):
        self.method = method



    """
    使用Http协议，向约定的ip:port发送http请求
    """
    def httpClient(self):
        # 定义需要进行发送的数据
        params = urllib.urlencode({'param': '6'});
        # 定义一些文件头
        headers = {"Content-Type": "application/x-www-form-urlencoded",
                   "Connection": "Keep-Alive", 'Content-length': '200'};

        response = None

        if 'GET' == self.method:
            response = self.httpGetRequest(params, headers)
        else:
            response = self.httpPostRequest(params, headers)

        # 1. response实例：
        # response 的实例：<addinfourl at 4488746120 whose fp = <socket._fileobject object at 0x10b6ebf50>> <type 'instance'>
        # 即：addinfourl(...) 这个对象
        print response, type(response)

        # 2. response.code
        if response.code == 200:
            print "发布成功!^_^!";
        else:
            print "发布失败\^0^/";

        # 3. response.readlines()
        linesInfo = response.readlines()
        print linesInfo, type(linesInfo)

        # 4. linesInfo[0]
        linesInfo_0 = linesInfo[0]
        print linesInfo_0, type(linesInfo_0)

        # 5. To python dict
        responseDict = json.loads(linesInfo_0)
        print responseDict, type(responseDict)

        # 取出约定值
        print 'code:' + responseDict['code']
        print 'msg:' + responseDict['msg']
        print 'data:' + responseDict['data']






    """
    GET 请求
    """
    def httpGetRequest(self, params, headers=None):
        request = urllib2.Request('http://127.0.0.1:8765?%s' %(params))

        response = urllib2.urlopen(request)
        return response



    """
    POST 请求
    """
    def httpPostRequest(self, params, headers=None):
        request = urllib2.Request('http://127.0.0.1:8765', params)
        response = urllib2.urlopen(request)
        return response



if __name__ == '__main__':
    thisObj = HttpClientDemo('GET1')
    thisObj.httpClient()