# coding:utf-8

"""
    break:
        中断循环
"""

count = 0
while count < 5:
    if count == 3:
        break
    print(count)
    count += 1
