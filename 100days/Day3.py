username = input("Please input username: ")
password = input("Please input password: ")

if username == 'admin' and password == '1111':
    print("sucess login")
else:
    print("failure!")

x = float(input("x = "))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))

x = float(input("x = "))
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print('f(%.2f) = %.2f' % (x,y))

value = float(input("Please input the length value: "))
unit = input("what is the unit: ")
if unit == 'in':
    value = value * 2.54
elif unit == 'cm':
    value = value / 2.54
else:
    print("Nooooooooooo")

score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('your level is', grade)

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a+b+c))
    p = (a+b+c)/2
    area = (p * (p-a)*(p-b)*(p-c))**0.5
    print('area is: %f' % (area))
else:
    print('cannot compute a triangle')
