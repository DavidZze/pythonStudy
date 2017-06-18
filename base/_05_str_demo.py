#! /usr/bin/python
# -*- coding=utf-8 -*-



def str_demo():
    log_line = "mapreduce.Job: The url to track the job: http://yq01-kg-resource0.yq01:8088/proxy/application_1490358783542_418865/"
    find_str = "The url to track the job: "
    not_find_str = "周泽"
    # 1. 匹配到的起始下标
    pos = log_line.find(find_str)
    print pos
    # 2. 如果find返回值为-1则表示没有匹配到
    pos_2 = log_line.find(not_find_str)
    print pos_2
    # 3. 字符串提取
    tracking_url = log_line[pos + len(find_str):].strip("\r\n")
    print "len(find_str)=", len(find_str)
    print tracking_url




def strip_demo():
    # 1. 默认去首尾后空格
    test_str = " 1234567890 1234567890 "
    print test_str
    test_str2 = test_str.strip()
    print test_str2

    # 2. 去除首尾指定的字符
    test_str = "abcd 1234567890 dd 1234567890 abcd"
    print test_str
    test_str2 = test_str.strip("d")
    print test_str2

    # 3. 去除首尾指定的特殊字符(回车，换行)
    test_str = "\r\n eeee 1234567890 dd 1234567890 eeee \r\n"
    print test_str
    test_str2 = test_str.strip("\r\n")
    print test_str2, (test_str == test_str2)



def split_demo():
    # 1. 分割字符串
    test_str = "2.7.0"
    print test_str.split(".")[0]



def rstrip():
    # 1. 仅删除末尾的指定字符
    test_str = "zzz 1234567890 1234567890 zz zzz"
    print test_str
    test_str2 = test_str.rstrip("z")
    print test_str2




if __name__ == '__main__':
    str_demo()
    strip_demo()
    split_demo()
    rstrip()