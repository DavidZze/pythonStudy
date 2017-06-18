#! /usr/bin/python
# -*- coding=utf-8 -*-


import select
import subprocess

class SubProcessDemo:

    """
    构造器
    """
    def __init__(self, pythonScript):
        self.python_scipt = pythonScript

    """
    获取PIPE所执行命令的标准输出，标准错误，
    并将标准输出与标准错误写入到日志文件。
    """
    def subProcessHandler01(self):

        result = subprocess.Popen(self.python_scipt, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # read date from pipe
        stdoutMsg = ""
        stderrMsg = ""
        readbuf_msg = ""
        readbuf_errmsg = ""

        # 缓冲区的大小
        # 当达到或者超过缓存区的大小再进行下一步处理
        buf_size = 1024

        select_rfds = [result.stdout, result.stderr]
        print len(select_rfds)

        while len(select_rfds) > 0:

            # 通过select 监听subProcess
            (rfds, wfds, efds) = select.select(select_rfds, [], [])

            # 标准输出处理
            if result.stdout in rfds:
                # 读取指定缓冲区大小的内容，达到或者超过才会进行下一步处理
                readbuf_msg = result.stdout.read(buf_size)
                if len(readbuf_msg) == 0:
                    select_rfds.remove(result.stdout)
                else:
                    print "zz-----" + readbuf_msg

            # 标准输入处理
            if result.stderr in rfds:
                readbuf_errmsg = result.stderr.read(buf_size)
                if len(readbuf_errmsg) == 0:
                    select_rfds.remove(result.stderr)
                else:
                    stderrMsg = stderrMsg + readbuf_errmsg

        # 等待字进程结束(等待shell命令结束)
        result.wait()

        exit_code = result.returncode
        print exit_code

        ##(stdoutMsg,stderrMsg) = result.communicate()#非阻塞时读法.
        str_ret = stdoutMsg + stderrMsg


    """
    更优雅的处理方式，
    不通过缓冲池，按行读取，这样时效性更好
    """
    def subProcessHandler02(self):

        # 开启子线程执行指定的shell命令
        result = subprocess.Popen(self.python_scipt, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # 标准输出与标准错误的数组（表）
        select_rfds = [result.stdout, result.stderr]

        # 通过While 循环 + select对subprocess的stdout, stderr进行监听
        while True:
            # 通过select 监听subProcess
            (rfds, wfds, efds) = select.select(select_rfds, [], [])

            # subprocess指向完则跳出当前循环
            if result.poll() is not None:
                break

            # 读取select的返回值dfds，并按行进行读取
            for pipe in rfds:
                text = pipe.readline()
                print "lt-----" + text


        # 等待字进程结束(等待shell命令结束), 感觉没啥用啊！！
        result.wait()
        exit_code = result.returncode
        print exit_code




if __name__ == '__main__':
    cmd = 'python /Users/zhouze/Documents/AppWorkspace/PycharmProjects/pythonStudy/socketStudy/_02_socketListener.py'
    thisObj = SubProcessDemo(cmd)
    thisObj.subProcessHandler02()


