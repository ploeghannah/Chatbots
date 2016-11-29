#!/usr/bin/env python

# Command Line Interface (CLI) version

import time
import rogerbot as bot
<<<<<<< HEAD
#
=======

>>>>>>> ArtezGDA/master

# Chat Server Framework functions

def sleep(n):
    """Sleep n number of seconds.
    Pauses the execution of the program.
    """
    time.sleep(n)


def output(s):
    """Outputs string s as chat message.
    Send the given string to the chat client.
    """
    print s


# Run forever on the command line

def main():
    """docstring for main"""
    # Setup
    bot.setup()
    #
    # Run continuesly
    while True:
        humanSpeak = raw_input("> ")
        bot.response(humanSpeak)
<<<<<<< HEAD
# > this means that u as a user should type something

if __name__ == '__main__':
    main()
# if u run the chatserever as a script itself it wil execute the main function,
#when we start the python script we run the main function
=======


if __name__ == '__main__':
    main()
>>>>>>> ArtezGDA/master
