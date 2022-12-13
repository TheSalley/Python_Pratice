username = input('请输入用户名:')
password = input('请输入口令:')

if username == 'admin' and password == 'admin':
    print('身份验证成功')
else:
    print('身份验证失败')

"""
    分段函数求值
            3x - 5 (x > 1)
    f(x) =  x + 2 (-1 <= x <= 1)
            5x + 3 (x < -1)
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))
