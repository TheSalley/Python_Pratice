# 将华氏温度转换为摄氏温度

f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8

print('%.1f华氏度 = %.1f摄氏度' % (f, c))

# 输入圆的半径计算周长和面积

radius = float(input('请输入圆的半径:'))
perimeter = 2 * 3.14 * radius
area = 3.14 * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)

# 判断输入的年份是不是闰年

year = int(input('请输入年份:'))
is_leap = year % 4 == 0 and year % 100 != 0 \
          or year % 400 == 0
print(is_leap)
