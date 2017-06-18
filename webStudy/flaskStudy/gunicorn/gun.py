#! /usr/bin/python
# -*- coding=utf-8 -*-


import gevent.monkey
gevent.monkey.patch_all()

import multiprocessing
import os,sys

import logging
from logging.handlers import TimedRotatingFileHandler,WatchedFileHandler
import re



base_path = os.path.dirname(os.path.abspath(__file__))


bind = '127.0.0.1:5000'
x_forwarded_for_header = 'X-FORWARDED-FOR'
# 超时时间，单位:seconds
# 超时指的是当前worker进程超时，处理超时gunicorn会kill当前进程。
timeout=20


# 日志配置(日志存放的目录必须存在，因为gunicorn不会辅助创建目录（Mac上测试），日志文件则可以交由gunicorn管理)
debug = True
loglevel = 'debug'
pidfile = base_path+ '/log/gunicorn.pid'
accesslog = base_path + '/log/access.log'
# accesslog = "/dev/null"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
errorlog = base_path + '/log/err.log'
# errorlog = "/dev/null"
# Redirect stdout/stderr to Error log.
capture_output = True

#
# log_fmt = '[gunicorn] ' + 'File:\"%(filename)s\" [%(asctime)s] line:%(lineno)s %(levelname)s:%(message)s'
#
#
# logging.basicConfig(level='DEBUG', format=log_fmt, stream=sys.stderr)


#
# logger_gunicorn_access = logging.getLogger('gunicorn.access')
# access_watch_handler = WatchedFileHandler(base_path + '/log/access.log')
# logger_gunicorn_access.addHandler(access_watch_handler)
# logger_gunicorn_access.propagate = False



# logger_gunicorn_error = logging.getLogger('gunicorn.error')
# formatter = logging.Formatter(log_fmt)
# filename = base_path.rstrip("/") + "/log/" + "server.out"
# log_file_handler = TimedRotatingFileHandler(filename=filename, when="D", interval=1,
#                         backupCount=5, encoding=None, delay=False, utc=True)
# log_file_handler.suffix = "%Y-%m-%d.log"
# log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
# log_file_handler.setFormatter(formatter)
# logger_gunicorn_error.addHandler(log_file_handler)
# logger_gunicorn_error.propagate = False



# logger_gunicorn_error = logging.getLogger('gunicorn.error')
# error_watch_handler = WatchedFileHandler(base_path + '/log/server.log')
# logger_gunicorn_error.addHandler(error_watch_handler)
# logger_gunicorn_error.propagate = False


#启动的进程数
workers = multiprocessing.cpu_count() * 2 + 1
# sync, gevent,meinheld gunicorn.workers.ggevent.GeventWorker , gunicorn.workers.base.Worker
worker_class = 'gunicorn.workers.ggevent.GeventWorker'




if __name__ == '__main__':
    print os.path.abspath(__name__)
    dir = os.path.dirname(os.path.abspath(__name__))
    print dir
    print dir.rstrip("/") + "/log/" + "all.out"