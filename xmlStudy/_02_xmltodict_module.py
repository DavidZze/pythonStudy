#! /usr/bin/python
# -*- coding=utf-8 -*-

import xmltodict
import os,json


class XMlToDictDemo:

    def __init__(self):
        pass

    def parse_xml(self):
        fd = open("./combine-generic_dy.xml", "r")
        doc = xmltodict.parse(fd.read())
        return doc

    def for_handler(self, config_dict):
        streaming_opt = ["file", "cacheFile", "cacheArchive", "input"]
        for property in streaming_opt:
            if property not in config_dict:
                print "[]"
                return []
            result = config_dict[property] if type(config_dict[property]) is type.ListType else [config_dict[property]]
            print result
            return result


if __name__ == "__main__":
    thisObj = XMlToDictDemo()
    doc = thisObj.parse_xml()

    # 1.
    config_dict = doc["configuration"]
    print config_dict

    # 2.
    thisObj.for_handler(config_dict)

    for key in config_dict:
        print key

    print "80" in config_dict