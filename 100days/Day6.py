# def factorial(num):
#     result = 1
#     for n in range(1, num + 1):
#         result *= n
#     return result
# m = int(input('m = '))
# n = int(input('n = '))
# print(factorial(m) // factorial(n) // factorial(m-n))

# from random import randint
# def roll_dice(n=2):
#     total = 0
#     for _ in range(n):
#         total += randint(1, 6)
#     return total

# def add(a=0, b=0, c=0):
#     return a+b+c

# print(roll_dice())
# print(roll_dice(3))

# print(add())
# print(add(1))
# print(add(1,2))
# print(add(1,2,3))
# print(add(c=50, a=100, b=200))

# def add(*args):
#     total = 0
#     for val in args:
#         total += val
#     return total

# print(add())
# print(add(1))
# print(add(1,2))
# print(add(1,2,3))
# print(add(1,2,3,4))

def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x, y):
    return x * y // gcd(x, y)

def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

def is_prime(num):
    if num == 1:
        return True
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False

if __name__ == '__main__':
    num = int(input('Please input a number:'))
    if is_palindrome(num) and is_prime(num):
        print('%d is a palindrome and a prime' % num)

