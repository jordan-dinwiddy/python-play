#!/usr/bin/python

# This is the third example defining function with variable number
# of arguments. This one is called 'Arbitrary Argument Lists'

def say_stuff(msg, *args):
	for i in args:
		print msg + ": " + i



say_stuff("Hello", "Fred", "Bob", "Johnny");
