class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def describeEmployee(self):
	return "name={}, salary={}".format(self.name, self.salary);

   def displayEmployee(self):
	# You have to refer to instance variables / fields using self.
	print self.describeEmployee();

   def __str__(self):
	return self.describeEmployee();
