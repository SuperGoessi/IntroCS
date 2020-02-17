# s1 = 'hello, world'
# s2 = "hello, world"
# s3 = """hello, 
# world!"""
# print(s1, s2, s3, end='')
# print()
# s1 = '\'hello, world\''
# s2 = '\n\\hello, world!\\\n'
# print(s1, s2, end='')
# print()
# s1 = r'\'hello, world!\''
# s2 = r'\n\\hello, world!\\\n'
# print(s1, s2, end='')

# s1 = 'hello' * 3
# print(s1)
# s2 = 'world'
# s1 += s2
# print(s1)
# print('li' in s1)
# print('good' in s1)
# str2 = 'abc123456'
# print(str2[2])
# print(str2[2:5])
# print(str2[2:])
# print(str2[2::2])
# print(str2[::2])
# print(str2[::-1])
# print(str2[-3:-1])

# str1 = 'hello, world'
# print(len(str1))
# print(str1.capitalize())
# print(str1.title())
# print(str1.upper())
# print(str1.find('or'))
# print(str1.find('shit'))
# print(str1.startswith('He'))
# print(str1.startswith('hel'))
# print(str1.endswith('!'))
# print(str1.center(50, '*'))
# print(str1.rjust(50, ' '))
# str2 = 'abc123456'
# print(str2.isdigit())
# print(str2.isalpha())
# print(str2.isalnum())
# str3 = '   j@haha.com '
# print(str3)
# print(str3.strip())

# a, b = 5, 10
# print(f'{a} * {b} = {a*b}')

# fruits = ['grape', 'apple', 'strawberry', 'waxberry']
# fruits += ['pitaya', 'pear', 'mango']
# print(fruits[-3:-1])

# list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# list2 = sorted(list1)
# list3 = sorted(list1, reverse=True)
# list4 = sorted(list1, key=len)
# print(list1)
# print(list2)
# print(list3)
# print(list4)
# list1.sort(reverse=True)
# print(list1)
# import sys
# f = [x for x in range(1, 10)]
# print(f)
# f = [x + y for x in 'ABCDE' for y in '1234567']
# print(f)
# f = [x ** 2 for x in range(1, 1000)]
# print(sys.getsizeof(f))
# # print(f)
# f = (x ** 2 for x in range(1, 1000))
# print(sys.getsizeof(f))
# print(f)
# for val in f:
#     print(val)

# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a

# def main():
#     for val in fib(20):
#         print(val)

# if __name__ == '__main__':
#     main()

# t = ('haha', 25, True, 'biu')
# print(t)
# print(t[0])
# print(t[3])
# for member in t:
#     print(member)
# t = ('hehe', 20, True, 'didi')
# print(t)
# person = list(t)
# print(person)
# person[0] = 'lala'
# person[1] = 25
# print(person)
# fruits_list = ['apple', 'banana','orange']
# fruits_tuple = tuple(fruits_list)
# print(fruits_tuple)

# set1 = {1,2,3,3,3,2}
# print(set1)
# print('Length = ', len(set1))
# set2 = set(range(1, 10))
# set3 = set((1, 2, 3, 3, 2, 1))
# print(set2, set3)
# set4 = {num for num in range(1, 100) if num%3 == 0 or num%5 == 0}
# print(set4)

# set1.add(4)
# set1.add(5)
# set2.update([11, 12])
# set2.discard(5)
# if 4 in set2:
#     set2.remove(4)
# print(set1, set2)
# print(set3.pop())
# print(set3)

# print(set1 & set2)
# print(set1 | set2)
# print(set1 - set2)
# print(set1 ^ set2)
# print(set2 <= set1)
# print(set3 <= set1)
# print(set1 >= set2)
# print(set1 >= set3)

# marks = {'haha':100, 'hehe':95, 'biubiu':90}
# print(marks)
# items1 = dict(one=1, two=2, three=3)
# print(items1)
# items2 = dict(zip(['a', 'b', 'c'],'123'))
# print(items2)
# items3 = {num: num**2 for num in range(1, 10)}
# print(items3)
# print(marks.pop('haha', 10))
# print(marks)

# import os
# import time

# def main():
#     content = 'welcome to wuhan...'
#     while True:
#         os.system('cls')
#         print(content)
#         time.sleep(0.2)
#         content = content[1:] + content[0]

# if __name__ == '__main__':
#     main()

# import random
# def generate_code(code_len=4):
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     last_pos = len(all_chars) - 1
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0, last_pos)
#         code += all_chars[index]
#     return code

# print(generate_code(8))

# def get_suffix(filename, has_dot=False):
#     pos = filename.rfind('.') + 1
#     if 0 < pos < len(filename) - 1:
#         index = pos if has_dot else pos + 1
#         return filename[index:]
#     else:
#         return ''

# print(get_suffix('haha.txt', True))

# def max2(x):
#     m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
#     for index in range(2, len(x)):
#         if x[index] > m1:
#             m2 = m1
#             m1 = x[index]
#         elif x[index] > m2:
#             m2 = x[index]
#     return m1, m2

# print(max2([1,2,34,56,1]))

# def is_leap_year(year):
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

# print([1,2,3][is_leap_year(400)])

# def which_day(year, month, date):
#     days_of_month = [[31,28,31,30,31,30,31,31,30,31,30,31],[31,29,31,30,31,30,31,31,30,31,30,31]][is_leap_year(year)]
#     total = 0
#     for index in range(month - 1):
#         total += days_of_month[index]
#     return total + date

# def main():
#     print(which_day(1980, 11, 28))
#     print(which_day(1981, 12, 31))
#     print(which_day(2010, 1, 1))
#     print(which_day(2016, 3, 1))

# if __name__ == '__main__':
#     main()

# def main():
#     num = int(input('Number of rows: '))
#     yh = [[]] * num
#     for row in range(len(yh)):
#         yh[row] = [None] * (row + 1)
#         for col in range(len(yh[row])):
#             if col == 0 or col == row:
#                 yh[row][col] = 1
#             else:
#                 yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
        
#     for i in range(num):
#         for j in range(num-i):
#             print(" ", end='')
#         for k in yh[i]:
#             print(k, end=' ')
#         for j in range(num-i):
#             print(" ", end='')
#         print()
        
        
# if __name__ == '__main__':
#     main()

def main():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                index %= 30
    for person in persons:
        print('k' if person else 'n', end='')

if __name__ == '__main__':
    main()

