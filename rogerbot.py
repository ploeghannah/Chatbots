#!/usr/bin/env python

# Default bot template

import chatServer as c
import random

def setup():
    global askedCounter
    askedCounter = 0
    c.output("Hello my name is Roger")
    c.sleep(1)
    c.output("wassup")

def response(input):
    #print(input)
    if not respondToTrigger(input):
        c.output(respondRandom())

def randomAssignments():
    answers = [
    "wurk tha tjetbox",
    "meek it work",
    "maak t gwn",
    "ik veeeettt echt niet"
    ]
    return random.choice(answers)
    #several answers

def respondToTrigger(input):
    triggers = ["assignment","opdracht","what do i do"]
    for t in triggers:
        if t in input:
            if askedCounter > 0:
                output("why do you ask me this again?")
            c.output(randomAssignments())
            askedCounter += 1
            return True
    return False
