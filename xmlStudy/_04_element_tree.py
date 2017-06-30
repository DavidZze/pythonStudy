#! -*- coding=utf-8 -*-


try:
  import xml.etree.cElementTree as ET
except ImportError:
  import xml.etree.ElementTree as ET
import sys


try:
  tree = ET.parse("./stone2.xml")     # 打开xml文档
  # root = ET.fromstring(country_string) # 从字符串传递xml
  root = tree.getroot()         # 获得root节点
  print root
except Exception, e:
  print "Error:cannot parse file:country.xml."
  sys.exit(1)


# 标签对象 => Element 实例对象
# 标签对象.tag => 标签名称
# 标签对象.txt => 标签的值
# 标签对象.attrib => 标签的属性dict
# Element是一个枚举类型的对象，枚举值为子标签Element实例对象
print type(root)
print root.tag, "---", root.attrib
for child in root:
  print child.tag, "---", child.attrib

# 通过下标访问
print "*"*10
print root[3], type(root[3])
print root[3].tag
print root[3][0].text
print root[3][1].text
for child in root[3]:
    print  type(child), child.tag, "-----", child.attrib
print "*"*10


# 常用的方法
# 1. Element.findall('标签名称'): 查询Element下所有的子Element list
# 2. Element.find('标签名称'): 查询Element下的第一个标签名相符的Element
# 3. Element.get('属性名'): 获取Element的指定属性对象值。
# 找到root节点下的所有job节点
print root.findall('job')
for job in root.findall('job'):
    name = job.get('name')  # 子节点下属性name的值
    job_name = job.find('name').text
    job_type = job.find('type').text
    job_input = job.find('input')
    if job_input is not None:
        input_type = job_input.get('logicIdentity')
        print type(job_input), '-----', input_type
    # print type(job), name, job_name, job_type, job_input


# 修改xml文件
# 1. Element.remove('Element'): 移除某个Element
# 2. Element.
for job in root.findall('job'):
    job_name = job.find('name').text
    if job_name == 'zhouze03':
        print job_name
        root.remove(job)
    elif job_name == 'David.ze':
        print job_name
        input_list = job.findall('input')
        print input_list
        for input in input_list:
            if input.get('id') == '1':
                input.set('logicIdentity', '/zz/01/')

tree.write('./output.xml')




