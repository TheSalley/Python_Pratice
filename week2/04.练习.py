# 输入一个正整数判断它是不是素数
from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)

# 输入两个正整数计算它们的最大公约数和最小公倍数
x = int(input('x = '))
y = int(input('y = '))
# 如果 x > y 就交换
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break

# 打印三角形
for i in range(1, 6):
    for j in range(1, i + 1):
        print('*', end='')
    print()

for i in range(6):
    for j in range(6):
        if i < 6 - 1 - j:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(6):
    for j in range(6 - 1 - i):
        print(' ', end='')
    for k in range(2 * i + 1):
        print('*', end='')
    print()
