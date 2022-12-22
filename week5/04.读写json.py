# coding:utf-8

"""
    json 模块：
        dump：将python对象按json 格式序列化到文件中
        load: 反序列化为对象
        dumps：将python对象处理成json 格式的字符串
        loads：反序列化为对象
"""

import json

mydict = {
    'name': 'alan',
    'age': 24,
    'friend': ['jack', 'mark']
}

try:
    f1 = open('04.data.json', 'w', encoding='utf-8')
    json.dump(mydict, f1)
except IOError:
    print('发生错误')
