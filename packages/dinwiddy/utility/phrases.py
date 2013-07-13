
def say_hello(name = None):
	if name != None:
		print 'Hello ' + name;
	else:
		print 'Hello';


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 :
    	say_hello(sys.argv[1]);
    else:
	say_hello();
