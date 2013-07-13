#!/usr/bin/python

# reduce(function, sequence) returns a single value constructed by calling the binary 
# function function on the first two items of the sequence, then on the result and the 
# next item, and so on. For example, to compute the sum of the numbers 1 through 10:

def add(x, y):
	return x + y;

print reduce(add, range(0, 10));
