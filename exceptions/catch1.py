#!/usr/bin/python

while True:
	try:
		x = int(raw_input("Please enter a number or zero to exit: "))
		if x == 0:
			break
	except ValueError:
		print "Oops!  That was no valid number.  Try again..."
