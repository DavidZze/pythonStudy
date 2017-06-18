#!/usr/bin/python
# -*- coding: utf-8 -*-

' 项目通用函数模块,提供项目相对于当前运行系统的路径 '

import sys,os

def projectSysPath():
    projectName = 'pythonStudy'
    currentPath = sys.path[0]
    print 'currentPath: ' + currentPath
    projectPath = currentPath.split(projectName)[0] + projectName
    print 'projectPath: ' + projectPath

    return projectPath


if __name__ == '__main__':
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    print cur_dir