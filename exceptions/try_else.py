#!/usr/bin/python

import sys

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print 'cannot open', arg
    # else is not the same as Java's finally. Instead else get's executed if there is no exception inside the try block
    # It's better than including the code in the try block since it stops you from accidentally catching exceptions
    # you weren't meaning to.
    else:
        print arg, 'has', len(f.readlines()), 'lines'
        f.close()
