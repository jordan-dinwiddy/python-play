#!/usr/bin/python

# Lambda's are restricted to a single expression in python.
# The lambda keyword is really just syntactic sugar for a
# normal function definition.

def make_incrementor(n):
	# return lambda x: x + n    the same as below
	return lambda(x): x + n

# This also works so I think a 'lambda' in python is identical
# to a normal nested function definition except that a lambda 
# is restricted to just a single expression
def make_incrementor2(n):
	def inc(x):
		return x + n;

	return inc;

my_func = make_incrementor(10);
print my_func(5);


my_func2 = make_incrementor2(11);
my_func3 = make_incrementor2(12);
print my_func2(5);
print my_func3(6);

print make_incrementor(13)(7);
