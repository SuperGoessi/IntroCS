# -*- coding: utf-8 -*-
"""

@author: JingQIN
"""

aList = [1,2,3,4,5]
aa = map(lambda x: x*2, aList)

listComprehension = [(x, y) for x in aList for y in aList]
print(listComprehension)

a = [1,2,3]
b = a
b.append(4)
c = a[:]
print(id(c))
print(id(a))

class Hammock():
    def __init__(self):
        self.sit = None
        self.pretry = None
        self.counter = 0
    
    def sitDown(self, aName):
        if self.sit == None:
            print("welcome!")
            self.sit = aName
        elif self.pretry == aName:
            print("welcome!")
            self.sit = aName
            self.counter += 1
        else:
            print("sorry, no room")
            self.pretry = aName
    
    def leave(self):
        print(self.counter)
        if self.counter != 0:
            self.counter -= 1
        
            
            
    

        