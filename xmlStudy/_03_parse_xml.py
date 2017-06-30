#! -*- coding=utf-8 -*-
"""
解析xml，与修改xml
"""

import xmltodict
import logging
import inspect
import json


def parse_xml():
    """
    解析
    :return:
    """
    xml_path = './stone2.xml'
    with open(xml_path) as fd:
        doc = xmltodict.parse(fd.read())
    logging.info(str(doc) + str(type(doc)))
    return doc


def get_stone_odict(doc_odict):
    """
    获取stone标签的内容
    :param doc_odict:
    :return:
    """
    stone_odict = doc_odict['stone']
    logging.info(stone_odict)
    return stone_odict


def get_job_list(stone_odict):
    """
    获取job标签内容List
    :param stone_odict:
    :return:
    """
    # 遍历odict
    for k1, v1 in stone_odict.items():
        # 获取所有job标签所组成的List
        if k1 == 'job':
            return v1


def get_job_input_list(job_odict):
    """
    获取job_input 标签list
    :param job_odict:
    :return:
    """
    for k, v in job_odict.items():
        if k == 'input':
            # 如果只有一个input标签
            if isinstance(v, dict):
                return [].append(v)
            else:
                return v


def dict_to_object(class_type, obj, dic):
    """
        将dict转化为已经预先定义好的Object。
        注意：
        dict的key 与 Class Object的属性名需要一致。
        备注：
        类对象与实例对象才允许执行
        :param class_type:
        :param obj:
        :param dic:
        :return:
        """
    if inspect.isclass(obj) or isinstance(obj, class_type):
        for k, v in dic.items():
            if hasattr(obj, k):
                setattr(obj, k, v)
        return obj


def get_exporse_input():
    """
    找到含有@exporse属性且属性值为Y的input标签。
    :return:
    """
    result_json = {}
    result_input_list = []

    doc_dict = parse_xml()
    stone_odict = get_stone_odict(doc_dict)
    job_list = get_job_list(stone_odict)
    for job_odict in job_list:
        # 获取当前job的input tag list
        job_input_list = get_job_input_list(job_odict)
        if job_input_list is not None:
            # 遍历list找到含有@exporse属性且属性值为Y的input标签
            for job_input_odict in job_input_list:
                for attr_name, attr_value in job_input_odict.items():
                    if attr_name == '@exporse' and attr_value == 'Y':
                        logging.info('****** %s: %s' % (job_odict['name'], job_input_odict))
                        job_input_odict['job_name'] = job_odict['name']
                        # logging.info(json.dumps(job_input_odict, default=lambda o: o.__dict__, sort_keys=True, indent=4))
                        result_input_list.append(job_input_odict)
    result_json['input_list'] = result_input_list
    logging.info(json.dumps(result_json, default=lambda o: o.__dict__, sort_keys=True, indent=4))
    return json.dumps(result_json)


if __name__ == '__main__':
    logging.getLogger().setLevel('DEBUG')
    print get_exporse_input()

    