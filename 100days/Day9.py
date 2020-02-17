# # class Person(object):

# #     __slots__ = ('_name', '_age', '_gender')

# #     def __init__(self, name, age):
# #         self._name = name
# #         self._age = age
    
# #     @property
# #     def name(self):
# #         return self._name
    
# #     @property
# #     def age(self):
# #         return self._age
    
# #     @age.setter
# #     def age(self, age):
# #         self._age = age

# #     def play(self):
# #         if self._age <= 16:
# #             print('%sis playing the chess.' % self._name)
# #         else:
# #             print('%sis playing the cards.' % self._name)
        
# # def main():
# #     person = Person('WANG', 12)
# #     person.play()
# #     person.age = 22
# #     person.play()

# # if __name__ == '__main__':
# #     main()

# # from math import sqrt

# # class Triangle(object):

# #     def __init__(self, a, b, c):
# #         self._a = a
# #         self._b = b
# #         self._c = c
    
# #     @staticmethod
# #     def is_valid(a, b, c):
# #         return a + b > c and b + c > a and a + c > b
    
# #     def perimeter(self):
# #         return self._a + self._b + self._c

# #     def area(self):
# #         half = self.perimeter() / 2
# #         return sqrt(half * (half - self._a)*(half - self._b)*(half - self._c))
    
# # def main():
# #     a, b, c = 3, 4, 5

# #     if Triangle.is_valid(a, b, c):
# #         t = Triangle(a, b, c)
# #         print(t.perimeter())
# #         print(t.area())
# #     else:
# #         print('cannot build a triangle')

# # if __name__ == '__main__':
# #     main()

# # from time import time, localtime, sleep

# # class Clock(object):
# #     def __init__(self, hour=0, minute=0, second=0):
# #         self._hour = hour
# #         self._minute = minute
# #         self._second = second

# #     @classmethod
# #     def now(cls):
# #         ctime = localtime(time())
# #         return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
    
# #     def run(self):
# #         self._second += 1
# #         if self._second == 60:
# #             self._second = 0
# #             self._minute += 1
# #             if self._minute == 60:
# #                 self._minute = 0
# #                 self._hour += 1
# #                 if self._hour == 24:
# #                     self._hour = 0

# #     def show(self):
# #         return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)

# # def main():
# #     clock = Clock.now()
# #     while True:
# #         print(clock.show())
# #         sleep(1)
# #         clock.run()

# # if __name__ == '__main__':
# #     main()

# class Person(object):
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
    
#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age
    
#     @age.setter
#     def age(self, age):
#         self._age = age
    
#     def play(self):
#         print('%s is playing happily.' % self._name)
    
#     def watch(self):
#         if self._age >= 18:
#             print('%s is watching TV.' % self._name)
#         else:
#             print('%s can read cartoon.' % self._name)
    

# class Student(Person):
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self._grade = grade

#     @property
#     def grade(self):
#         return self._grade
    
#     @grade.setter
#     def grade(self, grade):
#         self._grade = grade
    
#     def study(self, course):
#         print('%s got %s, is studying %s' % (self._name, self._grade, course))

# class Teacher(Person):
#     def __init__(self, name, age, title):
#         super().__init__(name, age)
#         self._title = title
    
#     @property
#     def title(self, title):
#         self._title = title
    
#     @title.setter
#     def title(self, title):
#         self._title = title
    
#     def teach(self, course):
#         print('%s%s is speaking %s.' % (self._name, self._title, course))


# def main():
#     stu = Student('hahaqin', 15, 'middle school')
#     stu.study('math')
#     stu.watch()
#     t = Teacher('biubiu', 28, 'expert')
#     t.teach('Python')
#     t.watch()

# if __name__ == '__main__':
#     main()

# from abc import ABCMeta, abstractmethod

# class Pet(object, metaclass=ABCMeta):
#     def __init__(self, nickname):
#         self._nickname = nickname
    
#     @abstractmethod
#     def make_voice(self):
#         pass

# class Dog(Pet):
#     def make_voice(self):
#         print('%s: wowowow...' % self._nickname)
    
# class Cat(Pet):
#     def make_voice(self):
#         print('%s: miaomiaomiao...' % self._nickname)

# def main():
#     pets = [Dog('A'), Dog('B'), Cat('C')]
#     for pet in pets:
#         pet.make_voice()

# if __name__ == '__main__':
#     main()

# from abc import ABCMeta, abstractmethod
# from random import randint, randrange

# class Fighter(object, metaclass=ABCMeta):
#     __slots__ = ('_name', '_hp')

#     def __init__(self, name, hp):
#         self._name = name
#         self._hp = hp
    
#     @property
#     def name(self):
#         return self._name
    
#     @property
#     def hp(self):
#         return self._hp
    
#     @hp.setter
#     def hp(self, hp):
#         self._hp = hp if hp >= 0 else 0
    
#     @property
#     def alive(self):
#         return self._hp > 0
    
#     @abstractmethod
#     def attack(self, other):
#         pass

# class Ultraman(Fighter):
#     __slots__ = ('_name', '_hp', '_mp')

#     def __init__(self, name, hp, mp):
#         super().__init__(name, hp)
#         self._mp = mp
    
#     def attack(self, other):
#         other.hp -= randint(15, 25)

#     def huge_attack(self, other):
#         if self._mp >= 50:
#             self._mp -= 50
#             injury = other.hp * 3 // 4
#             injury = injury if injury >= 50 else 50
#             other.hp -= injury
#             return True
#         else:
#             self.attack(other)
#             return False
    
#     def magic_attack(self, others):
#         if self._mp >= 20:
#             self._mp -= 20
#             for temp in others:
#                 if temp.alive:
#                     temp.hp -= randint(10, 15)
#             return True
#         else:
#             return False
    
#     def resume(self):
#         incr_point = randint(1, 10)
#         self._mp += incr_point
#         return incr_point
    
#     def __str__(self):
#         return '~~~%s Ultraman~~~\n' % self._name + \
#             'hp: %d\n' % self._hp + \
#             'mp: %d\n' % self._mp
    
# class Monster(Fighter):
#     __slots__ = ('_name', '_hp')

#     def attack(self, other):
#         other.hp -= randint(10, 20)

#     def __str__(self):
#         return '~~~%sMonster~~~\n' % self._name + 'hp: %d\n' % self._hp
# def is_any_alive(monsters):
#     for m in monsters:
#         if m.alive > 0:
#             return True
#     return False

# def select_alive_one(monsters):
#     monsters_len = len(monsters)
#     while True:
#         index = randrange(monsters_len)
#         monster = monsters[index]
#         if monster.alive > 0:
#             return monster

# def display_info(ultraman, monster):
#     print(ultraman)
#     for m in monster:
#         print(m, end=' ')
    
# def main():
#     u = Ultraman('biu', 1000, 120)
#     m1 = Monster('a', 250)
#     m2 = Monster('b', 500)
#     m3 = Monster('c', 750)
#     ms = [m1, m2, m3]

#     fight_round = 1

#     while u.alive and is_any_alive(ms):
#         print('===============%s ROUND=================' % fight_round)
#         m = select_alive_one(ms)
#         skill = randint(1, 10)
#         if skill <= 6:
#             print('normal attack, %s attacks %s' % (u.name, m.name))
#             u.attack(m)
#             print('resuming...%s with %s' % (u.name, u.resume()))
#         elif skill <= 9:
#             if u.magic_attack(ms):
#                 print('%s uses magic attack' % u.name)
#             else:
#                 print('%s failed with magic attack' % u.name)
#         else:
#             if u.huge_attack(m):
#                 print('%s killed %s' % (u.name, m.name))
#             else:
#                 print('normal attack, %s attacks %s' % (u.name, m.name))
#                 print('resuming...%s with %s' % (u.name, u.resume()))
#         if m.alive > 0:
#             print('%s fight back to %s' % (m.name, u.name))
#             m.attack(u)
#         display_info(u, ms)
#         fight_round += 1
#     print('===================end===================')
#     if u.alive > 0:
#         print("%s ultraman won" % u.name)
#     else:
#         print('Monster won')

# if __name__ == '__main__':
#     main()

