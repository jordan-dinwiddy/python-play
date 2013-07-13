#!/usr/bin/python

def fib(n):    # write Fibonacci series up to n
	"""Print a Fibonacci series up to n."""
	# The above line is called the docstring

	a, b = 0, 1
	while a < n:
		print a,
		a, b = b, a+b

fib(2000);

f = fib

f(100);

# Some might say that fib is really a procedure not a function
# because it doesn't return a value. In python it is a function
# and it returns a None. It's a special object
print f(0)
