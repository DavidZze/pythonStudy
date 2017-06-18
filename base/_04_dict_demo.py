#! /usr/bin/python
# -*- coding=utf-8 -*-


"""
dict update方法：
无则追加，有则更新
"""
def update_dict():

    old_dict = {"a":1, "b":2, "c":3}
    print old_dict, type(old_dict)

    #1. dict update
    new_dict = {"a":11, "b":"22", "c":33, "d":"xxx"}
    old_dict.update(new_dict)
    print old_dict

    add_dict = {"z":"000", "x":"000", "yyy":"000", "zzz":""}
    old_dict.update(add_dict)
    print old_dict

    return old_dict


"""
dict del
"""
def del_dict(dict):
    del dict["a"]
    print dict
    return  dict


if __name__ == "__main__":
    dict = update_dict()

    print "*"*40
    dict = del_dict(dict)

    print dict.get('c'),dict['c']
    # key不存在则赋值某个值
    print dict.get('go', '12345'), dict.get('go')
    print dict.get('zzz', 'zz123')
    # print dict.viewkeys(),type(dict.viewkeys()),dict.viewkeys().__iter__().next