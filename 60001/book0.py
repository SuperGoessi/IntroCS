# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 21:08:43 2019

@author: JingQIN
"""

#x = int(input("please enter a natural number: "))
#if x % 2 == 0:
#    if x % 3 == 0:
#        print('Divisible by 2 and 3')
#    else:
#        print('Divisible by 2 and not by 3')
#elif x % 3 == 0:
#    print('Divisible by 3 and not by 2')

#name = input('Enter your name: ')
#print('Are you really', name, '?')
#print('Are you really ' + name + '?')

#numXs = int(input('How many times should I print the letter X? '))
#toPrint = ''
#
#while (numXs != 0):
#    print('X')
#    numXs -= 1

#x = 4
#for i in range(0, x):
#    print(i)

#x = 4
#for i in range(0, x):
#    print(i)
#    x = 5

#x = 4
#for j in range(x):
#    for i in range(x):
#        print(i)
#        x = 2

# fine the cube root of a perfect cube
#x = int(input('Enter an integer: '))
#for ans in range(0, abs(x)+1):
#    if ans**3 >= abs(x):
#        break
#if ans**3 != abs(x):
#    print(x, 'is not a perfect cube')
#else:
#    if x < 0:
#        ans = -ans
#    print('Cube root of', x, 'is', ans)

#total = 0
#for c in '1235678':
#    total = total + int(c)
#print(total)

#s = '1.23,2.4,3.123'
#total = 0.0
#for i in s.split(','):
#    total += float(i)
#print(total)

#x = int(input('Enter an integer: '))
#ans = 0
#while ans**3 < abs(x):
#    ans = ans + 1
#if ans**3 != abs(x):
#    print(x, 'is not a perfect cube')
#else:
#    if x < 0:
#        ans = -ans
#    print('Cube root of', x, 'is', ans)

#maxVal = int(input('Enter a positive integer: '))
#i = 0
#while i < maxVal:
#    i = i + 1
#print(i)

# approximation solution
#x = 36
#epsilon = 0.01
#step = epsilon**2
#numGuesses = 0
#ans = 0.0
#while abs(ans**2 - x) >= epsilon and ans <= x:
#    ans += step
#    numGuesses += 1
#print('numGuesses =', numGuesses)
#if abs(ans**2 - x) >= epsilon:
#    print('Failed on square root of', x)
#else:
#    print(ans, 'is close to square root of', x)

#x = 25
#epsilon = 0.01
#numGuesses = 0
#low = 0.0
#high = max(1.0, x)
#
#ans = (high + low)/2.0
#while abs(ans**2 - x) >= epsilon:
#    print('low =', low, 'high =', high, 'ans =', ans)
#    numGuesses += 1
#    if ans**2 < x:
#        low = ans
#    else:
#        high = ans
#    ans = (high + low)/2.0
#print('numGuesses =', numGuesses)
#print(ans, 'is close to square root of', x)

x = 25
epsilon = 0.01
numGuesses = 0
if x < 0:
    low = x
    high = 0.0
else:
    low = 0.0
    high = x

ans = (high + low)/2.0

while abs(ans**3 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if abs(ans**3) < abs(x):
        if x < 0:
            low = x
            high = ans
        else:
            low = ans
            high = x
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to cube root of', x)