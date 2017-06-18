#! /usr/bin/python
# -*- coding=utf-8 -*-


import os
from osStudy.child_dir._02_path_study import PathStudy2

class PathStudy:

    def __init__(self):
        pass



    """
    1.
    ~代表用户目录，
    expanduser匹配参数的第一个~符号，并将当前的用户的用户目录替代~
    输入：~/xxxZZ.log
    输出：/Users/zhouze/xxxZZ.log
    """
    def path_handler(self):
        log_file = os.path.expanduser("~/xxxZZ.log")
        print log_file
        print '*'*40
        return log_file

    """
    2.
    os.path.basename
    说明：
    获取最后一个路径值,不能以/结尾（即不能是目录）
    输入：
    /Users/zhouze/xxxZZ.log
    输出：
    xxxZZ.log 
    """
    def base_name(self, log_file):
        dir_name = os.path.basename(log_file)
        print dir_name, type(dir_name)
        print '*' * 40


    """
    说明：
    os.path.dirname
    输入：
    路径
    返回：
    当前文件或者目录的父目录
    """
    def dir_name(self, dir_path):
        dir_name = os.path.dirname(dir_path)
        print dir_name, type(dir_name)
        print '*'*40
        return dir_name

if __name__ == "__main__":
    thisObj = PathStudy()
    # 1.
    log_file = thisObj.path_handler()
    # 2.
    # log_file = '/Users/zhouze'
    thisObj.base_name(log_file)
    # 3.
    thisObj.dir_name(log_file)

    # 4.
    path_study_2 = PathStudy2()
    path_study_2.path_test()


