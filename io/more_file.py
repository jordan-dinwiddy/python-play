#!/usr/bin/python

# open(filename, mode)
# mode can be r, w, a, r+
# for windows you can append b to the mode meaning 'binary' e.g:
#  rb, wb, r+b

filename = 'file.tmp'
print 'Writing data to {}...'.format(filename);
f = open(filename, 'a');
f.write("This is a test\n");
f.write("This is a second line\n");
f.write("This is a third line\n");
f.close();


print 'Reading data from {}...'.format(filename);
f = open(filename, 'r');

# You can loop over the file object to return a line
for line in f:
	print line;

f.close();

