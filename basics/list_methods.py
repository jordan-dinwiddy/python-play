#!/usr/bin/python

# Demo'ing the use of:
#  list.count - count the occurances of the given argument
#  list.insert - insert an item at a given position
#  list.append - append an item to the end of a list
#  list.index - returns the index of the first element matching the arg
#  list.remove - removes the first item in the list whose element matches the arg. Error if none.
#  list.reverse - reverse the elements, in place.
#  list.sort - sort the elements, in place.
#  list.pop - Removes the item at given position and returns it. If no arg, the last item is removed
# 
a = [66.25, 333, 333, 1, 1234.5];
print a.count(333), a.count(66.25), a.count('x');

a.insert(2, -1);
a.append(333);
print a;

a.index(333);
print a;

a.remove(333);
print a;

a.reverse();
print a;

a.sort();
print a;
