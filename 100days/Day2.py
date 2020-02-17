a = 321
b = 123
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

a = 100
b = 12.345
c = 1 + 5j
d = "hello, world"
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))

f = float(input("请输入华氏温度: "))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

import math
radius = float(input('please input radius: '))
p = 2*math.pi*radius
s = math.pi*(radius**2)
print("周长: %.2f" % p)
print("面积: %.2f" % s)

year = int(input('清楚如年份: '))
is_leap= (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(is_leap)
