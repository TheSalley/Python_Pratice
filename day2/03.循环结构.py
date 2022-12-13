import random

# 用for-in 循环实现 1 ~ 100 求和
"""
    range()
    range(101): 0 ~ 100
    range(1, 101): 1 ~ 100
    range(1, 101, 2): 1 ~ 100 的奇数 2 是步长
    range(100, 0, -2): 100 ~ 1 的偶数 -2 是步长
"""
sum = 0
for x in range(101):
    sum += x
print(sum)

# 猜数字游戏
answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了')
        # break
print('你一共猜了%d 次' % counter)

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d * %d = %d' % (i, j, i * j), end='\t')
    print()


