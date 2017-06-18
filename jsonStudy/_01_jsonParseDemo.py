#! /usr/bin/python
# -*- coding=utf-8 -*-

import json

class JsonParseDemo:

    def __init__(self):
        pass


    """
    1.
    将python dictionary >>>>> json对象
    """
    def dictionaryToJson(self , dicData):
        # json.dumps({...})
        json_str = json.dumps(dicData)
        return json_str



    """
    2.
    将json对象（str） >>>>> python dictionary
    """
    def jsonToDictionary(self, jsonStr):
        #json.loads(str)
        dic_data = json.loads(jsonStr)
        return dic_data


    """
    3. 
    将python dict写入json数据文件
    """
    def dictToJsonFile(self, dictData):
        # json.dump()
        with open('douban01.json', 'a', 0) as f:
            json.dump(dictData, f)
            f.write('\n')
            f.close()

    """
    4.
    从json数据文件中读取数据 并转换为 python dict
    """
    def jsonFileToDictObj(self):
        # json.load()
        with open('douban.json', 'r') as f:
            dictData = json.load(f)
            return dictData






if __name__ == '__main__':
    thisObj = JsonParseDemo()

    #1.
    dicData = {'name': 'ACME', 'shares': 100, 'price': 542.23333}
    json_str = thisObj.dictionaryToJson(dicData)
    print json_str, type(json_str)

    #2.
    dic_data = thisObj.jsonToDictionary(json_str)
    print dic_data, type(dic_data)

    #3.
    thisObj.dictToJsonFile(dic_data)

    #4.
    dic_data2 = thisObj.jsonFileToDictObj()
    print dic_data2, type(dic_data2)
    print dic_data2['famaliyData']