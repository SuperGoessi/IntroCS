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

#def isPalindrome(s):
#    def toChars(s):
#        s = s.lower()
#        ans = ''
#        for c in s:
#            if c in 'abcdefghijklmnopqrstuvwxyz':
#                ans = ans + c
#        return ans
#    
#    def isPal(s):
#        if len(s) <= 1:
#            return True
#        else:
#            return s[0] == s[-1] and isPal(s[1:-1])
#    return isPal(toChars(s))

#def lyrics_to_frequencies(lyrics):
#    myDict = {}
#    for word in lyrics:
#        if word in myDict:
#            myDict[word] += 1
#        else:
#            myDict[word] = 1
#    return myDict
#
#def most_common_words(freqs):
#    values = freqs.values()
#    best = max(values)
#    words = []
#    for k in freqs:
#        if freqs[k] == best:
#            words.append(k)
#            
#    return (words, best)

#def words_often(freqs, minTimes):
#    result = []
#    done = False
#    while not done:
#        temp = most_common_words(freqs)
#        if temp[1] >= minTimes:
#            result.append(temp)
#            for w in temp[0]:
#                del(freqs[w])
#        else:
#            done = True
#    return result

#def fib_efficient(n, d):
#    if n in d:
#        return d[n]
#    else:
#        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
#        d[n] = ans
#        return ans
#    
#d = {1:1, 2:2}
#print(fib_efficient(6, d))

# debug
#def get_ratios(L1, L2):
#    """ Assumes: L1 and L2 are lists of equal length of numbers
#    Returns: alist containing L1[i]/L2[i] """
#    ratios = []
#    for index in range(len(L1)):
#        try:
#            ratios.append(L1[index]/L2[index])
#        except ZeroDivisionError:
#            ratios.append(float('nan'))
#        except:
#            raise ValueError('get_ratios called with bad arg')
#    return ratios
#
#def avg(grades):
#    assert not len(grades) == 0, 'no grades data'
#    return sum(grades) / len(grades)

##OOP
#class Coordinate(object):
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
#        
#    def distance(self, other):
#        x_diff_sq = (self.x - other.x) ** 2
#        y_diff_sq = (self.y - other.y) ** 2
#        return (x_diff_sq + y_diff_sq)**0.5
#    
#    def __str__(self):
#        return "<" + str(self.x) + ", " + str(self.y) + ">"
#        
#
#c = Coordinate(3, 4)
#origin = Coordinate(0, 0)
#print(c.x)
#print(origin.x)
#print(c)
#
#class Fraction(object):
#    """
#    A number represented as a function
#    """
#    def __init__(self, num, denom):
#        """ num and denom are integers"""
#        assert type(num) == int and type(denom) == int
#        self.num = num
#        self.denom = denom
#    
#    def __str__(self):
#        """Returns a new fraction representing of self"""
#        return str(self.num) + "/" + str(self.ddenom)
    
#class Animal(object):
#    def __init__(self, age):
#        self.age = age
#        self.name = None
#    
#    def get_age(self):
#        return self.age
#    
#    def get_name(self):
#        return self.name
#    
#    def set_age(self, newage):
#        self.age = newage
#        
#    def set_name(self, newname=""):
#        self.name = newname
#    
#    def __str__(self):
#        return "animal:" + str(self.name) + ":" + str(self.age)
#    
#class Cat(Animal):
#    def speak(self):
#        print("meow")
#    def __str__(self):
#        return "cat: " + str(self.name) + ":" + str(self.age)
#    
#class Person(Animal):
#    def __init__(self, name, age):
#        Aminal.__init__(self, age)
#        self.set_name(name)
#        self.friends = []
#        
#    def get_friends(self):
#        return self.friends
#    
#    def add_friend(self, fname):
#        if fname not in self.friends:
#            self.friends.append(fname)
#            
#    def speak(self):
#        print("hello")
#        
#    def age_diff(self, other):
#        diff = self.age - other.age
#        print(abs(diff), "year difference")
#        
#    def __str__(self):
#        return "person:" + str(self.name) + ":" + str(self.age)
#import random   
#class Student(Person):
#    def __init__(self, name, age, major=None):
#        Person.__init__(self, name, age)
#        self.major = major
#    def change_major(self, major):
#        self.major = major
#    def speak(self):
#        r = random.random()
#        if r < 0.25:
#            print("i have homework")
#        elif 0.25 <= r < 0.5:
#            print("i need sleep")
#        elif 0.5 <= r < 0.75:
#            print("i should eat")
#        else:
#            print("i am watchng tv")
#    def __str__(self):
#        return "student: " + str(self.name) + ":" + str(self.age) + ":" + str(self.major)
#
#class Rabbit(Animal):
#    tag = 1
#    def __init__(self, age, parent1=None, parent2=None):
#        Animal.__init__(self, age)
#        self.parent1 = parent1
#        self.parent2 = parent2
#        self.rid = Rabbit.tag
#        Rabbit.tag += 1
#    def get_rid(self):
#        return str(self.rid).zfill(3)
#    def get_parent1(self):
#        return self.parent1
#    def get_parent2(self):
#        return self.parent2
#    def __eq__(self, other):
#        parents_same = (self.parent1.rid == other.parent1.rid\
#                       and self.parent2.rid == other.parents.rid)
#        parents_opposite = (self.parent1.rid == other.parent1.rid\
#                           and self.parent2.rid == other.parent2.rid)
#        return parents_same or parents_opposite
        
#import time 
#
#def c_to_f(c):
#    return c * 9 / 5 + 32
#
#t0 = time.clock()
#c_to_f(100000)
#t1 = time.clock() - t0
#print("t = ", t0, ":", t1, "s,")

#def bisect_search(L, e):
#    if L == []:
#        return False
#    elif len(L) == 1:
#        return L[0] == e
#    else:
#        half = len(L)//2
#        if L[half] > e:
#            return bisect_search(L[:half], e)
#        else:
#            return bisect_search(L[half:], e)

def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bizect_search_helper(L, e, 0, len(L) - 1)