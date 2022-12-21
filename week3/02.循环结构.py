# coding:utf-8

"""
    循环语句：
        for:
            支持 列表、字符串、元组、字典、集合
"""

count = 0
while count < 5:
    print(count)
    count += 1

print('*****')

count1 = 5
while count1 < 3:
    print(count1)
    count1 += 1
else:
    print(count1)

print('*****')

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)
