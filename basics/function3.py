#!/usr/bin/python

# We mentioned that functions can have a variable number of arguments.
# The first example of this was 'Default Arguments'.
# The second example will be 'Keyword Arguments'.

# Note that the formal parameters with defaults become 'optional' in the 
# calling context. The formal parameters without defaults are however 
# mandatory.
def printargs(desc, arg1='a', arg2='b', arg3='c'):
	print "arg1=" + arg1;
	print "arg2=" + arg2;
	print "arg3=" + arg3;


printargs("hey there");
printargs("hey there", arg3='my new value');
printargs(arg2='yo dude', desc='I am a desc and I never get printed');
