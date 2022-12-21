# coding:utf-8

"""
    分支语句
"""

if 3 > 1:
    print('3 > 1')

print('*****')

if 0 > 0:
    print('> 0')
elif 0 < 0:
    print('< 0')
else:
    print('0')

# 简写
a = -3
print('a is positive') if a > 0 else print('a is negative')
