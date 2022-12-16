# 字符串前加 r 取消转义

s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2)

# 运算符
s1 = 'hello ' * 3
print(s1)

s2 = 'world'
s1 += s2
print(s1)

print('a' in s1)
print('world' not in s1)

s3 = 'abc123456'
print(s3[2])  # c
print(s3[2:5])  # c12
print(s3[2:])  # c123456
print(s3[3::2])  # 135
print(s3[::2])  # ac246
print(s3[::-1])  # 654321cba
print(s3[1:-1])  # bc12345 左闭右开

s4 = 'hello, world!'
print(len(s4))
print(s4.capitalize())  # 字符串首字母大写
print(s4.title())  # 单词首字母大写
print(s4.upper())  # 变大写
print(s4.find('or'))  # 8
print(s4.find('sss'))  # -1
# index() 与find 类似，但找不到会报异常
print(s4.startswith('he'))  # True
print(s4.endswith('!'))  # True
# 将字符串以 指定的长度 居中 并在两侧填充指定的字符
print(s4.center(20, '*'))  # ***hello, world!****
# 将字符串以 指定的长度 靠右放置 并在左侧填充指定字符
print(s4.rjust(20, '!'))  # !!!!!!!hello, world!
print(s4.isdigit())  # False
print(s4.isalpha())  # False
print(s4.isalnum())  # False

a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
print(f'{a} * {b} = {a * b}')

"""
    列表
"""
list1 = [1, 3, 5, 7, 100]
print(len(list1))  # 5
list2 = ['a', 'b'] * 3
print(list2)  # ['a', 'b', 'a', 'b', 'a', 'b']

for index in range(len(list1)):
    print(list1[index])
for elem in list1:
    print(elem)
# 使用 enumerrate 函数处理列表后再遍历可以同时获取索引和值
for index, elem in enumerate(list1):
    print(index, elem)

"""
    向列表中添加、移除元素
"""
list3 = [1, 2, 3, 4, 5]
list3.append(6)
list3.insert(0, 0)
print(list3)
# 合并列表
list3.extend([100, 200])
print(list3)

if 3 in list3:
    list3.remove(3)
print(list3)  # [0, 1, 2, 4, 5, 6, 100, 200]
list3.pop(len(list3) - 1)
print(list3)  # [0, 1, 2, 4, 5, 6, 100]
list3.clear()
print(list3)  # []

"""
    列表的切片操作
"""
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
fruits2 = fruits[1:4]
print(fruits2)  # ['apple', 'strawberry', 'waxberry']
fruits3 = fruits[:]
print(fruits3)  # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']

"""
    元组
    元组中的元素是无法改变的
"""
t = ('TheShire', 23, True)
print(t)
# t[0] = '王大锤'  # TypeError
# 将元组转为列表
person = list(t)
print(person)
# 将列表转为元组
t2 = tuple(person)
print(t2)

"""
    集合
"""
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('length = ', len(set1))  # 3
