# coding:utf-8

"""
    集合：
        不重复，无序
"""

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)  # {'mango', 'banana', 'lemon', 'orange'}
print(len(fruits))   # 4

# 检查元素是否在集合中
print('apple' in fruits)  # False

# 增加
fruits.add('apple')
print(fruits)  # {'apple', 'lemon', 'orange', 'banana', 'mango'} 每次都会变

fruits.update(('onion',))
print(fruits)  # {'lemon', 'onion', 'mango', 'apple', 'banana', 'orange'}
fruits.update(['tomato'])
print(fruits)  # {'apple', 'banana', 'onion', 'mango', 'lemon', 'tomato', 'orange'}

print(fruits.union({'cabbage'}))  # {'onion', 'cabbage', 'mango', 'apple', 'lemon', 'orange', 'tomato', 'banana'}

# 删除
fruits.remove('onion')
print(fruits)  # {'mango', 'lemon', 'banana', 'apple', 'tomato', 'orange'}
fruits.pop()  # 随机删
print(fruits)

# del fruits

# 清空
fruits.clear()
print(fruits)  # set()

# 交集
st1 = {1, 2, 3}
st2 = {2, 3, 4}
print(st1.intersection(st2))  # {2, 3}

