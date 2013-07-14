#!/usr/bin/python

#Basic formatting
print "Hello {}, you are {} years old".format("Jo", 25);


# Formatting with padding
for x in range(1, 10):
	# Could also do {0:2d} {1:3d} {2:4d} where 0, 1, 2 are the position arguments
	print "{:2d} {:3d} {:4d}".format(x, x*x, x*x*x);


# Positional 
print "{0} and {1}".format("spam", "eggs");
print "{1} and {0}".format("spam", "eggs");

# Key words
welcome_str = "Hello {name}, you are {age} years old";
print welcome_str.format(name="Jo", age=25);

my_dict = {"name": "Jordan Dinwiddy", "age": 25};
print welcome_str.format(**my_dict);
print "Hello {0[name]}, you are {0[age]} years old".format(my_dict);

import math
print "The value of PI is approximately {0:.3f}.".format(math.pi);
