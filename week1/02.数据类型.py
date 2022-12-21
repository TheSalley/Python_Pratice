# coding:utf-8

"""
    数字、
    布尔值、
    None、
    字符串、
    元组、
    列表、
    集合、
    字典、
"""

# 数字：整数、浮点数、复数

apple_num = 12
price = 1.2
complex_num = 1 + 3j

# 布尔型：True、False

is_male = True


# None： 表示此数据类型不存在、未知或为空

def fun():
    pass


print(fun())  # None

# 字符串

name = 'alan'
word = """
    hello,
    world!
"""

# 元组：是不可变序列数据类型；可以包含多种混合数据类型；

fruits = ('orange', 'banner', 'apple')
mix = (1, 'alan', (0, 1, 2))

# 列表：是可变序列数据类型；

colors = ['red', 'yellow', 'blue']

# 集合：是无重复数据的无序数据集合；支持相交、并集等运算；

set1 = {'a', 'b', 'c', 'c', 'd'}
set2 = {'a', 'b', 'x', 'y', 'z'}

print(set1)  # {'a', 'b', 'c', 'd'}
print(set2)  # {'a', 'z', 'y', 'b', 'x'}
print(set1 & set2)  # {'a', 'b'}

# 字典：一组键值对

words = {
    'name': 'alan',
    'age': 22,
    'hobby': ['read book', 'play games', 'running']
}
