#!/usr/bin/python

# The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ), 
# and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) 
# and cannot be updated. Tuples can be thought of as read-only lists.

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print tuple           # Prints complete list
print tuple[0]        # Prints first element of the list
print tuple[1:3]      # Prints elements starting from 2nd till 3rd 
print tuple[2:]       # Prints elements starting from 3rd element
print tinytuple * 2   # Prints list two times
print tuple + tinytuple # Prints concatenated lists


singleton = ('hey');		# I dont actuall think this defines a tuple
singleton2 = 'hey',		# This does though

print singleton;
print singleton2;


# Tuple/sequence PACKING
elements = 'element 1', 'element 2', 'element 3';
print elements;

# tuple/sequence UNPACKING
element1, element2, element3 = elements;
print element1
print element2
print element3
