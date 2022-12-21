# coding:utf-8

"""
    字符串格式化：
        动态地将一些值放入字符串中。可以用 % 或 format() 方法实现
"""

print('There are %d oranges and %d apples in the basket' % (3, 2))
print('There are {0} oranges and {1} apples in the basket'.format(3, 2))


print('Height: %.2f %s' % (172.3, 'cm'))
print('Height: {0:.2f} {1:s}'.format(172.3, 'cm'))
