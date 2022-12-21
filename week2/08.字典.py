# coding:utf-8

"""
    字典：
        字典是键值对的容器。
"""

person = {
    'name': 'alan',
    'age': 24,
    'is_marred': False,
    'skill': ['JavaScript', 'Python', 'Node']
}
print(person)  # {'name': 'alan', 'age': 24, 'is_marred': False, 'skill': ['JavaScript', 'Python', 'Node']}
print(len(person))  # 4

# 根据键取值
print(person['age'])  # 24

print(person.get('name'))  # alan

# 增加
person['email'] = '123@xx.com'
print(person)
# {'name': 'alan', 'age': 24, 'is_marred': False, 'skill': ['JavaScript', 'Python', 'Node'], 'email': '123@xx.com'}

# 更改
person['name'] = 'alan turing'
print(person)
# {'name': 'alan turing', 'age': 24, 'is_marred': False, 'skill': ['JavaScript', 'Python', 'Node'], 'email': '123@xx.com'}

# 检查key 是否存在于字典中
print('name' in person)  # True

# 删除
person.popitem()  # 删除最后一个

person.pop('skill')
print(person)  # {'name': 'alan turing', 'age': 24, 'is_marred': False}

del person['is_marred']
print(person)  # {'name': 'alan turing', 'age': 24}

# del person

# 将字典改为列表
print(person.items())  # dict_items([('name', 'alan turing'), ('age', 24)])

# 获取由键组成的列表
print(person.keys())  # dict_keys(['name', 'age'])

# 获取由值组成的列表
print(person.values())  # dict_values(['alan turing', 24])

# 清空
print(person.clear())  # None
