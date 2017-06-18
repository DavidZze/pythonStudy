#! /usr/bin/python
# -*- coding=utf-8 -*-


from flask import Flask
import time
from restfultools import *
import threading

import logging
import sys

"""
测试结论：
原生的flask 接收的请求为阻塞模式，只有一个request处理完成
才会处理下一个request， 这显然不符合要求。
"""


logging.basicConfig(level='DEBUG', stream=sys.stderr)

app = Flask(__name__)

@app.route('/api/handler', methods=['GET'])
def asyc_handler():
    """
    阻塞测试：
    :return:
    """
    print get_curr_time()

    # 开启一个线程进行异步调用处理xx函数
    t1 = threading.Thread(target=long_time_func)
    t1.setDaemon(True)
    t1.start()

    print "no block"

    return fullResponse(R200_OK, "call test_asyc_handler() finished -----")

def get_curr_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def long_time_func():
    print 'start long_time_func'
    time.sleep(3)
    file_fd = open('./sleep2.log', 'a+', 1)
    file_fd.write(' -- long_time_func() execute finisher ----' + str(get_curr_time()))
    file_fd.write('\n')
    file_fd.close()
    logging.info(' -- flask logging flask logging flask logging flask logging flask logging ----' + str(get_curr_time()))
    print ' --print print print print print print print  ----' + str(get_curr_time())
    sys.stderr.write(' ------- stderr stderr stderr stderr stderr stderr  ----------- \n')


@app.route('/api/author', methods=['GET'])
def get_author():
    return fullResponse(R200_OK, "zhozue----author--- zzzz")


if __name__ == '__main__':
    app.run(debug=True)


