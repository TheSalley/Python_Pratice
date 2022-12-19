"""
    Python 的标准库和三方库 很多，很丰富，日常开发中可以直接使用它们解决问题。
"""

"""
    base64
    一种基于64个可打印字符表示二进制数据的方法。
    A ~ Z, a ~ z, 0 ~ 9, +, /, =  其中= 号用于最后进行补位
    函数：
        b64encode, b64decode 编码，解码
"""

import base64

content = 'Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure.'

print(base64.b64encode(content.encode()))
