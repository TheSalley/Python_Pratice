# coding:utf-8

"""
    continue:
        中断本次循环，继续下次循环
"""

count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1
