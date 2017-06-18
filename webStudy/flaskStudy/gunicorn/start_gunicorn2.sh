#! /bin/bash

unicorn_path=/Users/zhouze/Documents/AppWorkspace/PycharmProjects/pythonStudy/webStudy/flaskStudy/gunicorn


cd /Users/zhouze/Documents/AppWorkspace/PycharmProjects/pythonStudy/webStudy/flaskStudy/
# gunicorn -c ${unicorn_path}/gun2.py  --log-file=${unicorn_path}/log/all.out  wsgi:application
gunicorn -c ${unicorn_path}/gun2.py  wsgi:application

