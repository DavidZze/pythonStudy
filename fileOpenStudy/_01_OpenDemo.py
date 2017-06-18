#! /usr/bin/python
# -*- coding=utf-8 -*-

import subprocess,select

class OpenDemo:

    def __init__(self,shellCmd):
        self.shellCmd = shellCmd


    def writeLogFlie(self):
        # 开启子线程执行指定的shell命令
        result = subprocess.Popen(self.shellCmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # 标准输出与标准错误的数组（表）
        select_rfds = [result.stdout, result.stderr]

        # 需要写入的日志文件
        """
        缓冲的目的：
        是为了减少系统的io调用。只有当符合一定条件(比如缓冲数量)时才调用io。
        备注：
        个人觉得，缓冲1行比较符合日志的要求。
        """
        # 为0则表示无缓冲，有输入则立即写入磁盘
        # 为1则表示行缓冲，碰到换行就写入磁盘
        # >1则表示缓冲，数值为字节的数目，比如设置为N，则表示达到N个字节就像磁盘写。
        log1_fd = open('./log01', 'a+', 0)
        log2_fd = open('./log02', 'a+', 1)
        print log1_fd
        print 'log1_fd=' + str(log1_fd)
        print 'log2_fd=' + str(log2_fd)

        # 通过While 循环 + select对subprocess的stdout, stderr进行监听
        while True:
            # 通过select 监听subProcess
            (rfds, wfds, efds) = select.select(select_rfds, [], [])

            # subprocess指向完则跳出当前循环
            if result.poll() is not None:
                log1_fd.close()
                log2_fd.close()
                break

            # 读取select的返回值dfds，并按行进行读取
            for pipe in rfds:
                text = pipe.readline()
                log1_fd.write(text)
                log2_fd.write(text)
                print "lt-----" + text

        # 等待字进程结束(等待shell命令结束), 感觉没啥用啊！！
        result.wait()
        exit_code = result.returncode
        print exit_code



if __name__ == '__main__':
    shellCmd = 'python /Users/zhouze/Documents/AppWorkspace/PycharmProjects/pythonStudy/socketStudy/_02_socketListener.py'
    thisObj = OpenDemo(shellCmd)
    thisObj.writeLogFlie()
