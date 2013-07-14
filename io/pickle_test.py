#!/usr/bin/python

import pickle

outfile = "picklefile.tmp";
to_pickle = {"name": "Jordan Dinwiddy", "age": 25, "phone": "123-123-1234"};

print "I'm going to try and pickle the following to {}...: {}\n".format(outfile, to_pickle);

f = open(outfile, 'wb');
pickle.dump(to_pickle, f);
f.close();

print "All done!\n";
