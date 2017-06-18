#! /usr/bin/python
# -*- coding=utf-8 -*-

import xmltodict
import os,json

class XmlToDict:

    def __init__(self):
        pass

    """
    xml 对象转为 OrderedDict (有序字典)
    """
    def xml_to_dict(self):
        # curr_path = os.path.dirname(os.path.realpath(__file__))
        # conf_path = curr_path + "/stone.xml"
        conf_path = "./stone.xml"
        print conf_path

        # 1.
        with open(conf_path, 'r') as fd:
            # print fd, type(fd)
            doc = xmltodict.parse(fd.read())
        print doc, type(doc)

        # 2.
        fd2 = open(conf_path, 'r')
        doc2 = xmltodict.parse(fd2.read())
        print doc2, type(doc2)

        return doc2


    """
    属性的提取需要加@ 前缀
    """
    def draw_dict_info(self, xml_dict):

        # 0. 提取stone.name
        print "<stone><name> = " , xml_dict["stone"]["name"]

        # 1.
        stone_job_idtrans = xml_dict["stone"]["job"][1]
        print stone_job_idtrans
        # 2.
        stone_job_idtrans_config = stone_job_idtrans["configuration"]
        print stone_job_idtrans_config
        # 3. 属性的提取
        stone_job_idtrans_config_streaming = stone_job_idtrans_config["@streaming"]
        print stone_job_idtrans_config_streaming, type(stone_job_idtrans_config_streaming)

    """
    转换为Json格式
    """
    def draw_dict_to_json(self, xml_dict):
        configuration = xml_dict["stone"]["job"][1]["configuration"]
        json_conf = json.dumps(configuration, ensure_ascii=False)

        print configuration
        print json_conf, type(json_conf)







if __name__ == '__main__':
    thisObj = XmlToDict()
    xml_dict = thisObj.xml_to_dict()

    for key in xml_dict:
        print key

    # thisObj.draw_dict_info(xml_dict)
    # thisObj.draw_dict_to_json(xml_dict)
