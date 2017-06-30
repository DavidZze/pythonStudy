#! -*- coding=utf-8 -*-
import inspect


class Friends:
    def __init__(self, name = None, grade = None, age = None):
        self.name = name
        self.grade = grade
        self.age = age
    def __str__(self):
        return 'Friends: name=%s, grade=%s, grade=%s'% (self.name, self.grade, self.age)

    def test(self):
        print 'test'


class Friends2:
    def __init__(self):
        self.name = None
        self.grade = None
        self.age = None
    def __str__(self):
        return 'Friends: name=%s, grade=%s, grade=%s'% (self.name, self.grade, self.age)


class Friends3:
    def __init__(self, name , grade , age ):
        self.name = name
        self.grade = grade
        self.age = age
    def __str__(self):
        return 'Friends: name=%s, grade=%s, grade=%s'% (self.name, self.grade, self.age)


def dict_to_obj(classType, obj, adict):
    """
    类对象与实例对象才允许执行
    :param classType:
    :param obj:
    :param adict:
    :return:
    """
    # print inspect.isclass(Friends)
    # print isinstance(Friends(), Friends)
    if inspect.isclass(obj) or isinstance(obj, classType) :
        for k,v in adict.items():
            setattr(obj, k , v)
        return obj
    else:
        print 'error'

friends = [
        Friends('zhouze', 'boy', 20),
        Friends('liuting', 'girl', 18)
        ]


if __name__ == '__main__':
    print "*" * 60

    f1_dict = friends[0].__dict__
    f1_dict['zz']="zz"
    print  f1_dict

    print "*" * 60

    f2 =  dict_to_obj(Friends, Friends, f1_dict)
    print f2,f2.grade,f2.name,f2.age, type(f2)
    print isinstance(f2, Friends)
    # print f2.test()

    f3 = dict_to_obj(Friends, Friends(), f1_dict)
    print f3, f3.grade, f3.name, f3.age, type(f3)
    print isinstance(f3, Friends)

    print "*"*60

    f2 = dict_to_obj(Friends2, Friends2, f1_dict)
    print f2, f2.grade, f2.name, f2.age, type(f2)
    print isinstance(f2, Friends)

    f3 = dict_to_obj(Friends2, Friends2(), f1_dict)
    print f3, f3.grade, f3.name, f3.age, type(f3)
    print isinstance(f3, Friends)

    print "*" * 60

    f3 = dict_to_obj(Friends3, Friends3, f1_dict)
    print f3, f3.grade, f3.name, f3.age, type(f3)
    print isinstance(f3, Friends)


    # f3 = dict_to_obj(Friends3, Friends3(), f1_dict)
    # print f3, f3.grade, f3.name, f3.age, type(f3)
    # print isinstance(f3, Friends)

    f3 = Friends(name='zzlt')
    print f3

