import math

class Circle:

   def area(self,r):
       return math.pi * r ** 2

n=int(raw_input("Enter radius:"))
c=Circle()
print(c.area(n))
