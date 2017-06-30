#! -*- coding=utf-8 -*-

import json
from _02_flask_restplus_demo import api



print json.dumps(api.__schema__)


