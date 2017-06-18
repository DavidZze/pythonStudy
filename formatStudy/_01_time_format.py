#! /usr/bin/python
# -*- coding=utf-8 -*-

import time

class TimeFormat:

    def __init__(self):
        pass


    def format_by_time(self):
        now_time = int(time.time())
        print now_time, type(now_time)

        # 1. 获取元组(tuple)形式的时间戳
        now_time1 = time.localtime(now_time)
        print now_time1

        # 2. 结构化为最终需要的格式
        now_time2 = time.strftime('%Y-%m-%d', now_time1)
        print now_time2

        # 3.
        now_time3 = time.strftime("%Y-%m-%d_%H:%M:%S", now_time1)
        print now_time3

        print "/data/%s_%s" % ('xxxx', now_time3)

        # 简单可读形式
        print time.asctime(time.localtime(time.time()))



    def format_by_datetime(self):
        now_time = int(time.time())
        print now_time




if __name__ == '__main__':
    thisObj = TimeFormat()
    thisObj.format_by_time()

