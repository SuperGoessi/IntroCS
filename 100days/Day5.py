# # find amsterang number

# for num in range(100, 1000):
#     low = num%10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)

# # reverse the input number

# num = int(input("Please input the number: "))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num = num // 10
# print(reversed_num)

# # find x, y, z according to limitations
# for x in range(0, 20):
#     for y in range(0, 33):
#         z = 100 - x - y
#         if 5*x + 3*y + z == 100:
#             print('x = %d, y = %d, z = %d' % (x, y, z))

# from random import randint

# money = 1000
# while money > 0:
#     print('you have money: ', money)
#     needs_go_on = False
#     while True:
#         debt = int(input("Please put money: "))
#         if 0 < debt <= money:
#             break
#     first = randint(1, 6) + randint(1, 6)
#     print("you got number %d" % first)
#     if first == 7 or first == 11:
#         print("you win!")
#     elif first == 2 or first == 3 or first == 12:
#         print("others win!")
#         money -= debt
#     else:
#         needs_go_on = True
#     while needs_go_on:
#         needs_go_on = False
#         current = randint(1, 6) + randint(1, 6)
#         print('you got number %d' % current)
#         if current == 7:
#             print("others win")
#             money -= debt
#         elif current == first:
#             print('you win')
#             money += debt
#         else:
#             needs_go_on = True
# print("you have no money")

# count = 0
# first_num = 1
# second_num = 1
# sum_two = 0
# print(first_num, end = " ")
# print(second_num, end = " ")
# while count < 20:
#     sum_two = first_num + second_num
#     print(sum_two, end = ' ')
#     first_num = second_num
#     second_num = sum_two
#     count += 1

# for i in range(10000):
#     count = 0
#     for j in range(1, i):
#         if (i%j) == 0:
#             count += j
#     if count == i:
#         print(i)

for i in range(1, 100):
    count = 0
    for j in range(2, i):
        if i%j == 0:
            count += 1
    if count == 0:
        print(i)


