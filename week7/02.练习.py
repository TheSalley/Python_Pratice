# coding:utf-8
from math import sqrt

"""
    将1 ~ 9999 之间的素数分别写入3个文件中
    1 ~ 99 => a.txt
    100 ~ 999 => b.txt
    1000 ~ 9999 => c.txt
"""


def is_prime(n):
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False

filenames = ('02.a.txt', '02.b.txt', '02.c.txt')
fs_list = []
try:
    for filename in filenames:
        fs_list.append(open(filename, 'w', encoding='utf-8'))
    for number in range(1, 10000):
        if is_prime(number):
            if number < 100:
                fs_list[0].write(str(number) + '\n')
            elif number < 1000:
                fs_list[1].write(str(number) + '\n')
            else:
                fs_list[2].write(str(number) + '\n')
except IOError:
    print('写文件时发生错误')
finally:
    for fs in fs_list:
        fs.close()