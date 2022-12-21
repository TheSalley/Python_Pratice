# coding:utf-8

"""
    capitalize(): 第一个词的首字母大写
    title(): 每个词的首字母大写
    swapcase(): 大小写互转
    count(): 统计次数
    startswith(): 判断开头处的子串是否与之相符
    endswith(): 判断末尾处的子串是否与之相符
    expandtabs(): 将\t 替换为 指定长度的空格， 默认 8
    find(): 返回匹配到的子串的索引
    index(): 同find()
    注意：
        find 和 index 的区别：
            当找不到子串时，前者返回 -1，后者引发 ValueError 异常
    isalnum(): 检查是否全是字母、数字
    isalpha(): 检查是否全是字母
    isdigit(): 检查是否全是数字
    join(): 以某字符串作为分隔符拼接
    strip(): 去除首位的空字符串
    replace(): 替换子串
    split(): 切割字符串为列表

"""

word = 'life is short, use python.'
print(word.capitalize())  # Life is short, use python.
print(word.title())  # Life Is Short, Use Python.
print('a A'.swapcase())  # A a

print(word.count('t', 13, len(word) - 1))  # 1

print(word.startswith('life'))  # True
print(word.endswith('on.'))  # True

print('a\tb\tc'.expandtabs(1))  # a b c

print(word.find('is'))  # 5
print(word.index('is'))  # 5

print('a1 '.isalnum())  # False
print(word.isalpha())  # False
print('12'.isdigit())  # True

print('#'.join(['1', '2', '3']))  # 1#2#3
print('   a  '.strip())  # a
print(word.replace('python', 'javascript'))  # life is short, use javascript.
print('a,b'.split(','))  # ['a', 'b']


