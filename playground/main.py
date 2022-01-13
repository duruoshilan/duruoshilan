from ast import IsNot
from unit1.lesson2 import *

def isok():
    moveForward()
    moveForward()
    toggleSwitch()

    turnLeft()
    turnLeft()
    moveForward()
    turnRight()

    moveForward()
    collectWord()
    moveForward()
    collectWord()
    moveForward()
    moveForward()
    collectWord()
    moveForward()
    moveForward()
    
    turnLeft()
    moveForward()
    moveForward()

    collectWord()

def notok():
    moveForward()
    turnLeft()
    moveForward()
    collectWord()
    moveForward()
    collectWord()
    moveForward()
    moveForward()
    collectWord()
    moveForward()

def work():
    notok()
    # isok()



game.play(work)
