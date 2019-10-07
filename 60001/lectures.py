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

