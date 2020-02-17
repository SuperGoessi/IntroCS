# Loop

# though be familar with them, better to start from the basic

sum = 0
for x in range(101):
    sum += x
print(sum)

sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)

sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum)

# import random

# answer = random.randint(1, 100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('Please enter: '))
#     if number < answer:
#         print("Please enter bigger")
#     elif number > answer:
#         print("Please enter smaller")
#     else:
#         print("Congratulations!")
#         break

# print("You have gussed %d times" % counter)
# if counter > 7:
#     print("emmmmmmmmmm")

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (i, j, i*j), end ='\t')
#     print()

# from math import sqrt

# num = int(input("Please input a number: "))
# end = int(sqrt(num))
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break

# if is_prime and num != 1:
#     print('%d is a prime' % num)
# else:
#     print('%d is not a prime' % num)

# x = int(input("please input x: "))
# y = int(input("please input y: "))

# if x > y:
#     x, y = y, x

# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('largest factor number %d' % (x,y, factor))
#         print('smallest number %d'% (x,y, x*y//factor))
#         break

for i in range(0,5):
    for j in range(0,i + 1):
        print('*', end='')
    print()

for i in range(0,5):
    for j in range(0, 4-i):
        print(' ', end = '')
    for k in range(i+1):
        print('*', end = '')
    print()

row = int(input("Please input the number of the row: "))

for i in range(1,row+1):
    for j in range(0, row-i):
        print(' ', end = '')
    for k in range(2*i - 1):
        print('*', end = '')
    print()
