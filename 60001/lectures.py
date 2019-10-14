# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 20:22:24 2019

@author: JingQIN
"""

# lecture 01

#text = input("Type anything ...")
#print(5*text)
#
#num = int(input("Type a number..."))
#print(5*num)

#x = float(input("Enter a number for x: "))
#y = float(input("Enter a number for y: "))
#
#if x == y:
#    print("x and y are equal")
#    if y != 0:
#        print("therefore, x / y is", x/y)
#elif x < y:
#    print("x is smaller")
#else:
#    print("y is smaller")
#print("thanks!")

#n = input("You're in the Lost forest, go left or right?")
#while n == "right":
#    n = input("You're in the Lost forest, go left or right?")
#print("You got out of the Lost Forest!")

#haha = 'skalaljshf'
#print(len(haha))
#
#s = 'abcdfgke'
#for index in range(len(s)):
#    if s[index] == 'i' or s[index] == 'u':
#        print("There is an i or u")
#        
#for char in s:
#    if char == 'i' or char =='u':
#        print("There is an i or u")
#        
#
#an_letters = "aefhilmnorsxAEFHILMNORSX"
#word = input("I will cheer for you! Enter a word: ")
#times = int(input("Enthusiasm level (1-10): "))
#
#i = 0
#while i < len(word):
#    char = word[i]
#    if char in an_letters:
#        print("Give me an " + char +"! " + char)
#    else:
#        print("Give me a " + char + "! " + char)
#    i += 1
#print("What does that spell?")
#for i in range(times):
#    print(word, "!!!")

#cube = 8
#for guess in range(abs(cube)+1):
#    if guess**3 >= abs(cube):
#        break
#if guess**3 != abs(cube):
#    print(cube, 'is not a perfect cube')
#else:
#    if cube < 0:
#        guess = - guess
#    print('Cube root of ' + str(cube) + ' is ' + str(guess))

#cube = 27
#epsilon = 0.1
#guess = 0.0
#increment = 0.01
#num_guesses = 0
#
#while abs(guess**3 - cube) >= epsilon and guess <= cube:
#    guess += increment
#    num_guesses += 1
#print('num_guesses =', num_guesses)
#if abs(guess**3 - cube) >= epsilon:
#    print('Failed on cube root of', cube, 'with these parameters')
#else:
#    print(guess, 'is close to the cube root of', cube)

#def is_even(i):
#    """
#    Input: i, a positive int
#    Returns True if i is even, otherwise False
#    """
#    
##    print("inside is_even")
#    return i%2 == 0
#
#print(is_even(3))
#
#def f(x):
#    x = x + 1
#    print('in f(x) : x =', x)
#    return x
#
#x = 3
#z = f(x)
#
#print("All numbers between 0 and 20: even or not")
#
#for i in range(20):
#    if is_even(i):
#        print(i, "even")
#    else:
#        print(i, "odd")

#x = 0.0
#for i in range(10):
#    x = x + 0.1
#if x == 1.0:
#    print(x, '=1.0')
#else:
#    print(x, 'is not 1.0')

#def get_data(aTuple):
#    nums = ()
#    words = ()
#    for t in aTuple:
#        nums = nums + (t[0],)
#        if t[1] not in words:
#            words = words + (t[1],)
#            
#    min_n = min(nums)
#    max_n = max(nums)
#    unique_words = len(words)
#    return (min_n, max_n, unique_words)
#
#test = ((1, "a"), (2, "b"), (1, "a"), (7, "b"))
#(a, b, c) = get_data(test)
#print("a:", a, "b:", b, "c:", c)

#L = [1,2,3]
#total = 0
#for i in range(len(L)):
#    total += L[i]
#print(total)
#
#total = 0
#for i in L:
#    total += i
#print(total)

#s = "I<3 cs"
#print(list(s))
#
#print(s.split('<'))
#
#L = ['a', 'b', 'c']
#print(''.join(L))
#print('_'.join(L))

#def remove_dups(L1, L2):
#    for e in L1:
#        if e in L2:
#            L1.remove(e)
#
#L1 = [1,2,3,4]
#L2 = [1,2,5,6]
#
#remove_dups(L1, L2)
#
#print(L1)
#
#def remove_dups1(L1, L2):
#    L1_copy = L1[:]
#    for e in L1_copy:
#        if e in L2:
#            L1.remove(e)
#
#L1 = [1,2,3,4]
#L2 = [1,2,5,6]
#
#remove_dups1(L1, L2)
#
#print(L1)  

#def mul(a, b):
#    if b == 1:
#        return 1
#    else:
#        return a + mul(a, b-1)

# Hanoi tower

#def printMove(fr, to):
#    print('move from ' + str(fr) + ' to ' + str(to))
#    
#def Towers(n, fr, to, spare):
#    if n == 1:
#        printMove(fr, to)
#    else:
#        Towers(n-1, fr, spare, to)
#        Towers(1, fr, to, spare)
#        Towers(n-1, spare, to, fr)
#
#def fib(x):
#    if x == 0 or x == 1:
#        return 1
#    else:
#        return fib(x-1) + fib(x-2)

def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))