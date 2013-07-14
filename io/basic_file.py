#!/usr/bin/python

# open(filename, mode)
# mode can be r, w, a, r+
# for windows you can append b to the mode meaning 'binary' e.g:
#  rb, wb, r+b

filename = 'file.tmp'
print 'Writing data to {}...'.format(filename);
f = open(filename, 'w');
f.write("This is a test\n");
f.close();

print 'Reading data from {}...'.format(filename);
f = open(filename, 'r');
input = f.read();	# no arg means read all data
f.close();
print 'I read the following:\n'
print input

