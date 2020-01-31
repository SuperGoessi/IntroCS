# -*- coding: utf-8 -*-
"""

@author: JingQIN
"""
# concept codes in Signals and Systems

# class wallFinder(sm.SM):
#     startState = None
#     def getNextValues(self, state, inp):
#         desiredDistance = 0.5
#         currentDistance = inp.sonars[3]
#         return (state.io.Action(fvel=currentDistance - desiredDistance, rvel=0))

class vendingMachine():
    
    def __init__(self):
        self.change = 0
        self.soda = False
        
    def transduce(self, aList):
        bList = []
        money = 0
        for i in aList:            
            if i == 'quarter':
                print('q')
                money += 25
            elif i == 'dispense':
                print('d')
                if money >= 75:
                    money = money - 75
                    self.soda = True
                    self.change = money
                    money = 0
            else:
                print('c')
                self.change = money
                money = 0
            bList.append([self.change, self.soda])
            self.soda = False
            self.change = 0
        return bList
        
# concept codes in chapter 5

# Y = X - RX
class Diff(sm.SM):
    def __init__(self, previousInput):
        self.startState = previousInput
    def getNextValues(self, state, inp):
        return (inp, inp-state)


class LTISM(sm.SM):
    def __init__(self, dCoeffs, cCoeffs):
        j = len(dCoeffs) - 1
        k = len(cCoeffs)
        
        self.cCoeffs = cCoeffs
        self.dCoeffs = dCoeffs
        self.startState = ([0.0]*j, [0.0]*k)
        
    def getNextValues(self, state, input):
        (inputs, outputs) = state
        inputs = [input] + inputs
        
        currentOutput = util.dotProd(outputs, self.cCoeffs) + util.dotProd(inputs, self.dCoeffs)
        
        return ((inputs[:-1], ([currentOutput] + outputs)[:-1]), currentOutput)
    
# Quiz 4

class Triangle(Signal):
    def __init__(self, h):
        self.height = h
        self.num = 0
    def sample(self, n):
        self.num = abs(n)
        a = height - self.num
        if a > 0:
            return a
        else:
            return 0
        

            
                
                    