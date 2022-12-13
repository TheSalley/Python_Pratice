# 整型

a = 321
b = 12

print(a + b)  # 333
print(a - b)  # 309
print(a * b)  # 3825
print(a / b)  # 26.75

# 浮点型

# 字符串类型

# 布尔型

# 复数型

"""
    type() 检查数据类型
"""

a1 = 100
b1 = 12.345
c1 = 1 + 5j
d1 = 'hello, world'
e1 = True

print(type(a1))  # <class 'int'>
print(type(b1))  # <class 'float'>
print(type(c1))  # <class 'complex'>
print(type(d1))  # <class 'str'>
print(type(e1))  # <class 'bool'>

"""
    Python 内置的函数对数据的类型进行转换：
    
    int(): 将一个数值或字符串转为整数
    float(): 将一个字符串转为浮点型
    str(): 转为字符串类型
    chr(): 将证书转换为该编码对应的字符串(一个字符)
    ord(): 将字符串(一个字符)转为对应的编码
"""

"""
    input(): 获取键盘输入(字符串)
"""
1
a2 = int(input('a = '))
b2 = int(input('b = '))

print('%d + %d = %d' % (a2, b2, a2 + b2))
print('%d - %d = %d' % (a2, b2, a2 - b2))
print('%d * %d = %d' % (a2, b2, a2 * b2))
print('%d / %d = %f' % (a2, b2, a2 / b2))
print('%d // %d = %d' % (a2, b2, a2 // b2))  # //: 整除
print('%d %% %d = %d' % (a2, b2, a2 % b2))
print('%d ** %d = %d' % (a2, b2, a2 ** b2))  # **: 指数

