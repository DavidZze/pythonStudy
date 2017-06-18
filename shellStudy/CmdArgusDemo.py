#! /usr/bin/python
# -*- coding=utf-8 -*-

import argparse
import os


class CmdArgusDemo:

    def __init__(self):
        pass


    def pathHandler(self):
        # 解析命令行参数
        parse = argparse.ArgumentParser()
        parse.add_argument('-d', '--plugin-dir', dest='plugin_dir', required=True, help='user stone app director path')
        args = parse.parse_args()
        plugin_dir=args.plugin_dir
        print 'plugin_dir: ' + plugin_dir
        print plugin_dir.rstrip("/")

        plugin_dir02 = os.path.abspath(args.plugin_dir)
        print plugin_dir02
        print os.path.exists(plugin_dir)

        # 测试：创建一个/mkdirZZ 目录
        mkdirZZ = plugin_dir + '/mkdirZZ'
        print os.path.exists(mkdirZZ)

        if not os.path.exists(mkdirZZ):
            os.mkdir(mkdirZZ)
        print os.path.exists(mkdirZZ)




if __name__ == '__main__':
    thisObj = CmdArgusDemo()
    thisObj.pathHandler()




