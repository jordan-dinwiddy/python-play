#!/usr/bin/python

class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()

# SO private fields aren't really hidden... they are just renamed.
print counter._JustCounter__secretCount
print counter.__secretCount

