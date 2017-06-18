#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys

projectName = 'pythonStudy'

currentPath = sys.path[0]
print 'currentPath: ' + currentPath
projectPath = currentPath.split(projectName)[0] + projectName
print 'projectPath: ' + projectPath



print '------------------------------------------------'
print currentPath.split('AppWorkspace')
print 'abcdefg12345---+=/!'.split('12345')

