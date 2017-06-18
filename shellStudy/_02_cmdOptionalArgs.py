#! /usr/bin/python
# -*- coding: utf-8 -*-


import argparse


class CmdOptionalArgs:

    def __init__(self):
        pass



    # 短选项 - 的处理
    def handlerShortItem0(self):
        # 获取参数解析对象
        parse = argparse.ArgumentParser()
        # 定义参数：可选参数
        # parse.add_argument("-v",help='increase output verbosity', action='store_true')
        # 要求-v 是必选的参数。(required)
        # 要求 -v 短选项的参数值被 verbose接收 （dest）
        parse.add_argument("-v", "--verbose2" ,dest= 'verbose', help='increase output verbosity', required = True)
        # 解析并提取参数
        args = parse.parse_args()
        # 获取定义的参数值
        print '--short---args.verbose: ' + str(args.verbose)
        if args.verbose:
            print "v turned on"


    # 短选项 - 的处理
    def handlerShortItem(self):
        # 获取参数解析对象
        parse = argparse.ArgumentParser()
        # 定义参数：可选参数
        parse.add_argument("-v", "--verbose", help='increase output verbosity', action = 'store_true')
        # 解析并提取参数
        args = parse.parse_args()
        # 获取定义的参数值
        print '--short---args.verbose: ' + str(args.verbose)
        if args.verbose:
            print "verbosity turned on"



    # 长选项 --  的处理
    def handlerLongItem(self):
        # 获取参数解析对象
        parse = argparse.ArgumentParser()
        # 定义参数：可选参数
        # action='store_true' 表示该长选项后面不需要参数值（即写--verbose 即有约定的含义，理解为无参数的函数方法即可）
        parse.add_argument("--verbose", help = 'increase output verbosity', action = 'store_true')
        # 解析并提取参数
        args = parse.parse_args()
        # 获取定义的参数值
        print '-----args.verbose: ' + str(args.verbose)
        if args.verbose:
            print "verbosity turned on"



if __name__ == '__main__':
    thisObj = CmdOptionalArgs()
    # thisObj.handlerLongItem()
    # thisObj.handlerShortItem()
    thisObj.handlerShortItem0()

