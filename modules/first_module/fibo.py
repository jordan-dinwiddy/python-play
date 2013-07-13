# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

# The __name__ variable stores the name of the current module
def whoami():
	print __name__

# A convenient way of testing a module. Basically if this module is run directly using
# `python fib.py` then the below is run because the __name__ variable is not set to
# the module name but instead to __main__
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))


