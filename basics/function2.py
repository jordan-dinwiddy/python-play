#!/usr/bin/python

# It is possible to define function with variable arguments. There
# are 3 forms. The first one is 'Default Arguments'.
# It's worth realising that the default argument is evaluated 
# only once during function defintion and in the defining
# scope. So the default value can itself be a variable aslong
# as that variable is defined at the point the function 
# is defined.
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
	while True:
		ok = raw_input(prompt)
		if ok in ('y', 'ye', 'yes'):
            		return True
        	
		if ok in ('n', 'no', 'nop', 'nope'):
            		return False
        
		retries = retries - 1
        	if retries < 0:
            		raise IOError('refusenik user')
        	print complaint

print ask_ok("Hey man, please enter something:");
