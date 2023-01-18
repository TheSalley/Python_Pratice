# coding:utf-8

"""
    操作模式：
        r 读取（默认）
        w 写入（会先截断之前的内容）
        x 写入，如果文件已存在会产生异常
        a 追加内容至文件末尾
        b 二进制模式
        t 文本模式（默认）
        + 更新（可读可写）
"""
# f = None
# try:
#     f = open('01.data.txt', 'r', encoding='utf-8')
#     print(f.read())
# except FileNotFoundError:
#     print('无法打开指定的文件')
# except LookupError:
#     print('指定了未知的编码')
# except UnicodeDecodeError:
#     print('读取文件时解码错误')
# finally:
#     if f:
#         f.close()

# 关键字with 在不在需要访问文件时自动关闭
with open('01.data.txt', 'w', encoding='utf-8') as file_object:
    contents = file_object.write(
"""杜甫 <<春夜喜雨>>
好雨知时节，当春乃发生。
随风潜入夜，润物细无声。
野径云俱黑，江船火独明。
晓看红湿处，花重锦官城。
"""
    )

"""
    for-in 循环
"""

# f = open('01.data.txt', 'r', encoding='utf-8')
# for line in f:
#     print(line, end='')
# print()

"""
    readlines 读所有行
"""

# f = open('01.data.txt', 'r', encoding='utf-8')
# lines = f.readlines()
# print(lines)
