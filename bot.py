#!/usr/bin/env python

# Default bot template

import chatServer as c
<<<<<<< HEAD

def setup():
    c.output("This is the bot template.")
    c.sleep(1)
    c.output('It does nothing more than just responding with "Ok".')

def response(input):
    print(input)
    c.output("Ok")

def respondRandom():
    answer = [
    "OK",
    "Roger",
    "Roger that",
    "acknowleged",
    "confirmat"
    ]
    c.output()
    #several answers
=======


# Sleep and output functions
def sleep(n):
    c.sleep(n)


def output(s):
    c.output(s)


def setup():
    output("This is the bot template.")
    sleep(1)
    output('It does nothing more than just responding with "Ok".')

    
def response(input):
    print(input)
    output("Ok")
>>>>>>> ArtezGDA/master
