#!/usr/bin/python

import pickle

infile = "picklefile.tmp";

print "I'm going to try and unpickle from {}...\n".format(infile);

f = open(infile, 'r');
data1 = pickle.load(f);
f.close();

print "All done! I got:\n";
print data1;
