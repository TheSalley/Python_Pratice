# coding:utf-8

"""
    函数：

"""


# 求阶乘的函数
def fac(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


print(fac(3))

print('*****')


# 参数名前的* 表示args 是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))
