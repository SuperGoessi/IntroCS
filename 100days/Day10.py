# def main():
#     f = None
#     try:
#         f = open('To you.txt', 'r', encoding='utf-8')
#         print(f.read())
#     except FileNotFoundError:
#         print('cannot open the file')
#     except LookupError:
#         print('assign unknown enncoding')
#     except UnicodeDecodeError:
#         print('read-in process error')
#     finally:
#         if f:
#             f.close()

# if __name__ == '__main__':
#     main()

import time

# def main():
#     with open('To you.txt', 'r', encoding='utf-8') as f:
#         print(f.read())
    
#     with open('To you.txt', mode='r') as f:
#         for line in f:
#             print(line, end='')
#             time.sleep(0.5)
#     print()

#     with open('To you.txt') as f:
#         lines = f.readlines()
#     print(lines)    

# if __name__ == '__main__':
#     main()

# from math import sqrt

# def is_prime(n):
#     assert n > 0
#     for factor in range(2, int(sqrt(n)) + 1):
#         if n % factor == 0:
#             return False
#     return True if n != 1 else False

# def main():
#     filenames = ('a.txt', 'b.txt', 'c.txt')
#     fs_list = []
#     try:
#         for filename in filenames:
#             fs_list.append(open(filename, 'w', encoding='utf-8'))
#         for number in range(1, 10000):
#             if is_prime(number):
#                 if number < 100:
#                     fs_list[0].write(str(number) + '\n')
#                 elif number < 1000:
#                     fs_list[1].write(str(number) + '\n')
#                 else:
#                     fs_list[2].write(str(number) + '\n')
#     except IOError as ex:
#         print(ex)
#         print('write-in error')
#     finally:
#         for fs in fs_list:
#             fs.close()
#     print("Well Done")

# if __name__ == '__main__':
#     main()

# def main():
#     try:
#         with open('a.jpg', 'rb') as fs1:
#             data = fs1.read()
#             print(type(data))
#         with open('b.jpg', 'wb') as fs2:
#             fs2.write(data)
#     except FileNotFoundError as e:
#         print("Cannot open it")
#     except IOError as e:
#         print('read/write error')
#     print('program ends')

#     if __name__ == '__main__':
#         main()

import json

def main():
    mydict = {
        'name': 'haha',
        'age': 38,
        'game': ['GTAV', 'fitness ring'],
        'cars': [{'brand':'BYD', 'max_speed':100}, {'brand':'Audi', 'max_speed':200}, {'brand':'Benz', 'max_speed':320}]
    }

    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print("Done")

if __name__ == '__main__':
    main()
    