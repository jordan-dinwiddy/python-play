#!/usr/bin/python

# To implement a queue we could use a basic list. However that's inefficient because
# the dequeue operation would basically be a list.pop(0) and each time that is called
# every element in the list has to be shifted.

# So, if you want an efficient queue try using the collections.deque package.

from collections import deque
queue = deque(["Element 1", "Element 2", "Element 3"]);
queue.append("Element 4");
queue.append("Element 5");

print queue.popleft();
print queue.popleft();

print queue;
