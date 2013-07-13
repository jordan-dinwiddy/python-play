#!/usr/bin/python

# Lists are pretty efficient for use as stacks since elements are only
# manipulated at the end of the list. That's not true for queue's mind.

stack = [3, 4, 5];

# Push to our stack
stack.append(6);
stack.append(7);


print stack;

# Pop some elements
print stack.pop();
print stack.pop();

print stack;
