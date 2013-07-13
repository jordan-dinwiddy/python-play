#!/usr/bin/python


# So python has sets in addition to lists, tuples, dictionaries

# You create a set using {...} (similar to dictionary expect you aren't passing in mappings)
# or using the set keyword.
# NOTE: {} creates an empty dictionary, NOT an empty set. If you want an empty set you have to use set()

# List of elements containing dupes
elements = ['element 1', 'element 2', 'element 1', 'element 3', 'element 2'];

# Create a set from existing elements
my_set = set(elements);
print elements;
print my_set;

# Create a set straight off
set2 = {'element 1', 'element 2'};
print set2;

# membership testing
print 'element 2' in set2;
print 'element 3' in set2;
