# -*- coding: utf-8 -*-
"""


@author: JingQIN
"""

# concept codes to control a robot using state machine

import sm
import io

class StopSM(sm.SM):
    def getNextValues(self, state, inp):
        return (None, io.Action())
    
    def setup():
        robot.behavior = StopSM()
        robot.behavior.start()
        
    def step():
        robot.behavior.step(io.SensorInput(), verbose = False).execute()
        
class RotateTSM(SM):
    rotationalGain = 3.0
    angleEpsilon = 0.01
    startState = 'start'
    
    def __init__(self, headingDelta):
        self.headingDelta = headingDelta
        
    def getNextValues(self, state, inp):
        currentTheta = inp.odometry.theta
        if state == 'start':
            thetaDesired = util.fixAnglePlusMinusPi(currentTheta + self.headingDelta)
        else:
            (thetaDesired, thetaLast) = state
        
        newState = (thetaDesired, currentTheta)
        action = io.Action(rvel = self.rotationalGain * util.fixAnglePlusMinusPi(thetaDesired - currentTheta))
        
        return (newState, action)
    
    def done(self, state):
        if state == 'start':
            return False
        else:
            (thetaDesired, thetaLast) = state
            return utl.nearAngle(thetaDesired, thetaLast, self.angleEpsilon)
        
class ForwardTSM(SM):
    forwardGain = 1.0
    distTargetEpsilon = 0.01
    startState= 'start'
    
    def __init__(self, delta):
        self.deltaDesired = delta
        
    def getNextValues(self, state, inp):
        currentPos = inp.odometry.point()
        if state == 'start':
            print "Starting forward", self.deltaDesired
            startPos = currentPos
        else:
            (startPos, lastPos) = state
        newState = (startPos, currentPos)
        error = self.deltaDesired - startPos.distance(currentPos)
        action = io.Action(fvel = self.forwardGain * error)
        return (newState, action)
    
    def done(self, state):
        if state == 'start':
            return False
        else:
            (startPos, lastPos) = state
            return util.within(startPos.distance(lastPos), self.deltaDesired, self.distTargetEpsilon)

class XYDriver(SM):
    forwardGain = 2.0
    rotationGain = 2.0
    angleEps = 0.05
    distEps = 0.02
    startState = False
    
    def getNextValues(self, state, inp):
        (goalPoint, sensors) = inp
        robotPose = sensors.odometry
        robotPoint = robotPose.point()
        robotTheta = robotPose.theta
        
        if goalPoint == None:
            return (True, ioAction())
        
        headingTheta = robotPoint.angleTo(goalPoint)
        if util.nearAngle(robotTheta, headingTheta, self.angleEps):
            # Pointing in the right direction, so move forward
            r = robotPoint.distance(goalPoint)
            if r < self.distEps:
                #we're there
                return (True, ioAction())
            else:
                return (False, io.Action(fvel = r * self.forwardGain))
        else:
            # Rotate to point toward goal
            headingError = util.fixAnglePlusMinusPi(headingTheta - robotTheta)
            
        return (False, io.Action(rvel = headingError * self.rotationGain))
        
class SpyroGyra(SM):
    distEps = 0.02
    def __init__(self, incr):
        self.incr = incr
        self.startState = ('south', 0, None)
        
    def getNextValues(self, state, inp):
        (direction, length, subGoal) = state
        robotPose = inp.odometry
        robotPoint = robotPose.point()
        if subGoal == None:
            subGoal = robotPoint
        if robotPoint.isNear(subGoal, self.distEps):
            # Time to change state
            length = length + self.incr
            if direction == 'east':
                direction = 'north'
                subGoal.y += length
            elif direction == 'north':
                direction = 'west'
                subGoal.x -= length
            elif direction == 'west':
                direction = 'south'
                subGoal.y -= length
            else: # south
                direction = 'east'
                subGoal.x += length
            print 'new:', direction, length, subGoal
            return ((direction, length, subGoal), (subGoal, inp))
        
        def spireFlow(incr):
            return sm.Cascade(SpyroGyra(incr), XYDriver())
        