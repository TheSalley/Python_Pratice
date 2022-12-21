# coding:utf-8

"""
    字符串：
        字符组成的序列。具有不可变性。
"""

# 字符串长度 len()

string = 'hello, world!'
print(len(string))  # 13

# 解构字符串

language = 'python'
a, b, c, d, e, f = language
print(a, b, c, d, e, f)  # p y t h o n

# 通过index 取值

first_letter = language[0]
print(first_letter)  # p

# 切片

first_three = language[0:3]
print(first_three)  # pyt
last_three = language[-3:]
print(last_three)  # hon
sub = language[0::2]
print(sub)  # pto

# 转义字符

print('hello, \nworld!')  # \n 换行
print('hello,\b\b\b\b')  # \b 退格
print(r'hello,\n\b world')  # 取消转义
