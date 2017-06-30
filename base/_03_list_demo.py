#! /usr/bin/python
# -*- coding=utf-8 -*-


class ListDemo:

    def __init__(self):
        self.cmd = []
        pass

    def list_demo(self):
        self.cmd.append('ps')
        self.cmd.append('-aux')
        self.cmd.append('|')
        self.cmd.append('grep')
        self.cmd.append('java')
        #
        self.__format_cmd()

        # extend 将一个列表追加到另一个列表
        cmd2 = ['|', 'grep', '-v', 'tomcat']
        self.cmd.extend(cmd2)
        self.__format_cmd()

        # 元组也可以用extend加入，因此元组也被称为定值表
        self.cmd.extend(('zz', '111'))
        self.__format_cmd()

    def __format_cmd(self):
        print self.cmd, type(self.cmd)
        format_cmd = " ".join(self.cmd)
        print format_cmd, type(format_cmd)


    def format_cmd_by_repr(self):
        print "*"*40
        print "%s\n" % (repr(" ".join(self.cmd)))
        print "%s\n" % (" ".join(self.cmd))


    def repr_demo(self):
        print "*"*40
        test_str = "abcdefg"
        print test_str == eval(repr(test_str))
        print test_str == eval(str(test_str))


if __name__ == '__main__':
    # thisObj = ListDemo()
    # thisObj.list_demo()
    #
    # thisObj.format_cmd_by_repr()
    # thisObj.repr_demo()


    lis = ['111', '222']
    print lis is list
    print type(lis) is list
    for item in lis:
        print item in []