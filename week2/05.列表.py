# coding:utf-8

"""
    列表：
        一些值的有序序列。
        列表是可变的，我们可以在它上面进行增删改查。
"""

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)  # ['banana', 'orange', 'mango', 'lemon']
print(len(fruits))  # 4

# 根据索引取值


second_fruit = fruits[1]
print(second_fruit)  # orange

# 切片
orange_and_mango = fruits[1:3]
print(orange_and_mango)  # ['orange', 'mango']

# 改值
fruits[0] = 'apple'
print(fruits)  # ['apple', 'orange', 'mango', 'lemon']

# 检查值是否在列表中
print('banana' in fruits)  # False

print(fruits.index('apple'))  # 0 找不到会报异常

# 增加
fruits.append('pear')
print(fruits)  # ['apple', 'orange', 'mango', 'lemon', 'pear']

fruits.insert(2, 'strawberry')
print(fruits)  # ['apple', 'orange', 'strawberry', 'mango', 'lemon', 'pear']

fruits += ['durian']
print(fruits)  # ['apple', 'orange', 'strawberry', 'mango', 'lemon', 'pear', 'durian']

fruits.extend(['watermelon'])
print(fruits)  # ['apple', 'orange', 'strawberry', 'mango', 'lemon', 'pear', 'durian', 'watermelon']

# 删除
fruits.remove('strawberry')
print(fruits)  # ['apple', 'orange', 'mango', 'lemon', 'pear']

fruits.pop(1)
print(fruits)  # ['apple', 'mango', 'lemon', 'pear']

del fruits[1]
print(fruits)  # ['apple', 'lemon', 'pear']

# 复制
fruits_copy = fruits.copy()
print(fruits_copy)  # ['apple', 'lemon', 'pear']

# 清空
fruits.clear()
print(fruits)  # []

# 反转
number_list = [1, 2, 3, 2]
number_list.reverse()
print(number_list)  # [2, 3, 2, 1]

# 排序
number_list.sort()
print(number_list)  # [1, 2, 2, 3]
