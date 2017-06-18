#! /bin/bash

unicorn_path=/Users/zhouze/Documents/AppWorkspace/PycharmProjects/pythonStudy/webStudy/flaskStudy/gunicorn/guni.conf


cd /Users/zhouze/Documents/AppWorkspace/PycharmProjects/pythonStudy/webStudy/flaskStudy/
gunicorn -c ${unicorn_path} wsgi:application

