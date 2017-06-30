#! -*- coding=utf-8 -*-

import json


class Customer:
    def __init__(self, name, grade, age, home, office, friends = None):
        self.name = name
        self.grade = grade
        self.age = age
        self.address = Address(home, office)
        self.friends = friends
    def __repr__(self):
        # return repr((self.name, self.grade, self.age, self.address.home, self.friends))
        return repr((self.name, self.grade, self.age, self.address.home))

class Address:
    def __init__(self, home, office):
        self.home = home
        self.office = office
    def __repr__(self):
        return repr((self.home, self.office))

class Friends:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def __str__(self):
        return 'Friends: name=%s, grade=%s'% (self.name, self.grade)
    # def __repr__(self):
    #     return repr((self.name, self.grade))




customers = [
        Customer('john', 'A', 15, '111', 'aaa'),
        Customer('jane', 'B', 12, '222', 'bbb'),
        Customer('dave', 'B', 10, '333', 'ccc'),
        ]

friends = [
        Friends('zhouze', 'boy'),
        Friends('liuting', 'girl')
        ]


def cux_dict_spilt(dic):
    key_str = ''
    values_list = []
    dict_index = 1
    dict_len = len(dic)
    for k,v in dic.items():
        if dict_index < dict_len:
            key_str += k + ','
        else:
            key_str += k
        values_list.append(v)
        dict_index += 1
    return key_str, tuple(values_list)



if __name__ == '__main__':
    # sort_keys = True 表示最终的输出将按照Key进行排序
    # indent = 4 表示json的格式将按照4个字符进行缩进
    # 推荐上面两个选项仅仅在日志显示时使用
    json_str = json.dumps(customers, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    # json_str = json.dumps(customers, default=lambda o: o.__dict__)

    print json_str

    # 一个Customer 有多个Friends
    customers[0].friends = friends
    json_str2 = json.dumps(customers, default=lambda o:o.__dict__, sort_keys=True, indent=4)
    print json_str2

    #
    customers_0_dict = customers[0].__dict__
    print customers_0_dict
    key_str, values_tuple = cux_dict_spilt(customers_0_dict)
    print key_str, values_tuple

