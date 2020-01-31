# -*- coding: utf-8 -*-
"""
Author: Jing Qin

This is book note of 6.01SC, chapter 4
"""

# chapter 4 state machines
class SM:
    startState = 0
    
    def getNextValues(self, state, inp):
        nextState = self.getNextValues(state, inp)
        return (nextState, nextState)
    
    def start(self):
        self.state = self.startState
        
    def step(self, inp):
        s = self.getNextValues(self.state, inp)
        self.state = s
        return s
    
    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]
    
    def run(self, n = 10):
        return self.transduce([None] * n)
    
    def done(self, state):
        return False
    
class Accumulator(SM):
    startState = 0
    
    def __init__(self, initialValue):
        self.startDtate = initialValue
    
    def getNextValues(self, state, inp):
        return state + inp
    
class Gain(SM):
    
    def __init__(self, k):
        self.k = k
    
    def getNextValues(self, state, inp):
        return inp * self.k
    
class ABC(SM):
    startState = 0
    def getNextValues(self, state, inp):
        if state == 0 and inp == 'a':
            return (1, True)
        elif state == 1 and inp == 'b':
            return (2, True)
        elif state == 2 and inp == 'c':
            return (0, True)
        else:
            return (3, False)

class UpDown(SM):
    startState = 0
    def getNextState(self, state, inp):
        if inp == 'u':
            return state + 1
        else:
            return state - 1
        
class Delay(SM):
    def __init__(self, v0):
        self.startState = v0
    def getNextValuse(self, state, inp):
        return (inp, state)
    
class Average(SM):
    startState = 0
    def getNextValues(self, state, inp):
        return (inp, (inp + state) / 2.0)
    
class SumLast3(SM):
    startState = (0, 0)
    def getNextValues(self, state, inp):
        (previousPreviousInput, previousInput) = state
        return ((previousInput, inp), previousPreviousInput + previousInput + inp)
    
class Select(SM):
    def __init__(self, k):
        self.k = k
    def getNextState(self, state, inp):
        return inp[self.k]
    
class SimpleParkingGate(SM):
    startState = 'waiting'
    
    def generateOutput(self, state):
        if state == 'raising':
            return 'raise'
        elif state == 'lowering':
            return 'lower'
        else:
            return 'nop'
        
    def getNextValues(self, state, inp):
        (gatePosition, carAtGate, carJustExited) = inp
        if state == 'waiting' and carAtGate:
            nextState = 'raising'
        elif state == 'raising' and gatePosition == 'top':
            nextState = 'raised'
        elif state == 'raised' and carJustExited:
            nextState = 'lowering'
        elif state == 'lowering' and gatePosition == 'bottom':
            nextState = 'waiting'
        else:
            nextState = state
        return (nextState, self.generateOutput(nextState))
    
class Increment(SM):
    def __init__(self, incr):
        self.incr = incr
    def getNextState(self, state, inp):
        return safeAdd(inp, self.incr)
    
class Parallel(SM):
    def __init__(self, sm1, sm2):
        self.m1 = sm1
        self.m2 = sm2
        self.startState = (sm1.startState, sm2.startState)
        
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (newS1, o1) = self.m1.getNextValues(s1, inp)
        (newS2, o2) = self.m2.getNextValues(s2, inp)
        return ((newS1, newS2), (o1, o2))
    
class Parallel2(Parallel):
    
    
    def splitValue(v):
        if v == 'undefined':
            return ('undefined', 'undefined')
        else:
            return v
        
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (i1, i2) = splitValue(inp)
        (newS1, o1) = self.m1.getNextValues(s1, i1)
        (newS2, o2) = self.m2.getNextValues(s2, i2)
        return ((newS1, newS2), (o1, o2))
    
class ParallelAdd(Parallel):
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (newS1, o1) = self.m1.getNextValues(s1, inp)
        (newS2, o2) = self.m2.getNextValues(s2, inp)
        return ((newS1, newS2), o1 + o2)

# feedback machine: that machine must not have a direct dependence of its output on its input

class Feedback(SM):
    def __init__(self, sm):
        self.m = sm
        self.startState = self.m.startState
        
    def getNextValues(self, state, inp):
        (ignore, o) = self.m.getNextValues(state, 'undefined')
        (newS, ignore) = self.m.getNextValues(state, o)
        return (newS, o)
    
    def makeCounter(init, step):
        return sm.Feedback(sm.Cascade(Increment(step), sm.Delay(init)))
        
class Wire(SM):
    def getNextState(self, state, inp):
        return inp

class Feedback2(Feedback):
    def getNextValues(self, state, inp):
        (ignore, o) = self.m.getNextValues(state, (inp, 'undefined'))
        (newS, ignore) = self.m.getNextValues(state, (inp, o))
        return (newS, o)
    
class Switch(SM):
    def __init__(self, condition, sm1, sm2):
        self.m1 = sm1
        self.m2 = sm2
        self.condition = condition
        self.startState = (self.m1.startState, self.m2.startState)
        
    def getNextValues(self, state, inp):
        (s1, s2) = state
        if self.condition(inp):
            (ns1, o) = self.m1.getNextValues(s1, inp)
            return ((ns1, s2), o)
        else:
            (ns2, o) = self.m2.getNextValues(s2, inp)
            return ((s1, ns2), o)

class Mux(Switch):
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (ns1, o1) = self.m1.getNextValues(s1, inp)
        (ns2, o2) = self.m2.getNextValues(s2, inp)
        if self.condition(inp):
            return ((ns1, ns2), o1)
        else:
            return ((ns1, ns2), o2)

class ConsumeFiveValues(SM):
    startState = (0, 0) #count, total
    
    def getNextValues(self, state, inp):
        (count, total) = state
        if count == 4:
            return ((count + 1, total + inp), total + inp)
        else:
            return ((count + 1, total + inp), None)
        
    def done(self, state):
        (count, total) = state
        return count == 5

class Repeat(SM):
    def __init__(self, sm, n = None):
        self.sm = sm
        self.startState = (0, self.sm.startState)
        self.n = n
        
    def advanceIfDone(self, counter, smState):
        while self.sm.done(smState) and not self.done((counter, smState)):
            counter = counter + 1
            smState = self.sm.startState
        return (counter, smState)
    
    def getNextValues(self, state, inp):
        (counter, smState) = state
        (smState, o) = self.sm.getNextValues(smState, inp)
        (counter, smState) = self.advanceIfDone(counter, smState)
        return ((counter, smState), o)
    
    def done(self, state):
        (counter, smState) = state
        return counter == self.n
    
class CharTSM(SM):
    startState == False
    
    def __init__(self, c):
        self.c = c
    def getNextValues(self, state, inp):
        return (True, self.c)
    def done(self, state):
        return state
 
class Sequence(SM):
    def __init__(self, smList):
        self.smList = smList
        self.startState = (0, self.smList[0].startState)
        self.n = len(smList)
        
    def advanceIfDone(self, counter, smState):
        while self.smList[counter].done(smState) and counter + 1 < self.n:
            counter = counter + 1
            smState = self.smList[counter].startState
        return (counter, smState)
    
    def getNextValues(self, state, inp):
        (counter, smState) = state
        (smState, o) = self.smList[counter].getNextValues(smState, inp)
        (counter, smState) = self.advanceIfDone(counter, smState)
        return ((counter, smState), o)
    
    def done(self, state):
        (counter, smState) = state
        return self.smList[counter].done(smState)
    
class RepeatUntil(SM):
    def __init__(self, condition, sm):
        self.sm = sm
        self.condition = condition
        self.startState = (False, self.sm.startState)
        
    def getNextValues(self, state, inp):
        (condTrue, smState) = state
        (smState, o) = self.sm.getNextValues(smState, inp)
        condTrue = self.condition(inp)
        if self.sm.done(smState) and not condTrue:
            smState = self.sm.getStartState()
        return ((condTrue, smState), o)
    
    def done(self, state):
        (condTrue, smState) = state
        return self.sm.done(smState) and condTrue

      