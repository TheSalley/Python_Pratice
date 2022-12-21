# coding:utf-8

"""
    元组：
        不可变
"""

fruits = ('banana', 'orange', 'mango')
print(fruits)  # ('banana', 'orange', 'mango')
print(len(fruits))  # 3

# 根据索引取值
first_fruit = fruits[0]
print(first_fruit)  # banana

# 切片
orange_and_mango = fruits[1:]
print(orange_and_mango)  # ('orange', 'mango')

# 将元组转为列表
lst = list(fruits)
print(lst)  # ['banana', 'orange', 'mango']

# 检查元素是否在元组中
print('apple' in fruits)  # False

# 增加
fruits += ('watermelon',)
print(fruits)  # ('banana', 'orange', 'mango', 'watermelon')

# 删除
del fruits
