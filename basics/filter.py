#!/usr/bin/python

# Define a filter function that returns true if the
# element is not divisible by 2 AND 3
def filter_func(x):
	return x % 2 != 0 and x % 3 != 0


print filter(filter_func, range(1, 25));
