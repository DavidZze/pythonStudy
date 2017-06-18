#! /usr/bin/python
# -*- coding=utf-8 -*-

from flask import Flask
from restfultools import *


app = Flask(__name__)

@app.route('/')
def index():
    return fullResponse(R200_OK, "hello world! -zz")





if __name__ == "__main__":
    app.run(debug=True)







