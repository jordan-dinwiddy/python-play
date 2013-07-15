#!/usr/bin/python

from employee import Employee 

emp1 = Employee("Bob", 50000);
emp2 = Employee("Mary", 60000);

print emp1;
print emp2;

emp1.displayEmployee();
emp2.displayEmployee();
emp1.displayCount();

# Because python is dynamic and all you can add attributes to an 
# existing instance
emp1.age = 25;

