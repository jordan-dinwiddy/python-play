#!/usr/bin/python


# The map function applies a given function to each element inside a list and returns 
# the return value (it doesn't make the changes in place);

def square(x):
	return x*x;

def screw_up_list(l):
	l[3] = 1020;

my_list = range(1, 10);
print my_list;
print map(square, my_list);
print my_list;
screw_up_list(my_list);
print my_list;


# You can have 2 params to the map function in which case you must
# have 2 args in your applied function
def add(x, y):
	return x + y;

print map(add, range(1, 10), range(1, 10));
