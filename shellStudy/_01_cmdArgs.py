#! /usr/bin/python
# -*- coding: utf-8 -*-

import argparse


# argparse 是Python自带的模块，用于解析shell command的命令行参数


class CmdArgs:


    def __init__(self, author = 'zhouze' ):
        self.author = author
        pass

    def getArgs01(self):
        # 获取命令行解析器
        parse = argparse.ArgumentParser()
        args = parse.parse_args()

    def getArgs02(self):
        # 获取命令行解析器
        parse = argparse.ArgumentParser()
        # 设置程序可接受的命令行参数, Help帮助用户理解参数的作用
        parse.add_argument("echo", help="echo the string you use here")
        # parse_args() 会从命令行参数中获取到内容
        args = parse.parse_args()
        print args.echo

    def getArgs03(self):
        # 获取命令行参数解析器
        parse = argparse.ArgumentParser()
        # 设置当前python脚本可以接受的命令行参数， help为该参数功能的描述 , 并指定参数的数据类型
        parse.add_argument("square" , help = 'display a square of a given number' , type = int)
        # 解析并提取命令行中的参数内容
        args = parse.parse_args()
        print args.square**3




if __name__ == '__main__':
    thisObj = CmdArgs('zhouze03')
    # thisObj.getArgs01()
    thisObj.getArgs03()