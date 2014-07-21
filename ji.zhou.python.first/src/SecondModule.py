'''
Created on 18 Jul 2014

@author: Ji Zhou Gash
'''

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "x-value " + str(self.x) + " y-value " + str(self.y)
    def __add__(self,other):
        p = Point()
        p.x = self.x+other.x
        p.y = self.y+other.y
        return p
        
    def __sub__(self,other):
        p = Point()
        p.x = self.x - other.x
        p.y = self.y - other.y
        return p
        
    def __Mul__(self,other):
        p = Point()
        p.x = self.x * other.x
        p.y = self.y * other.y
        return p
    
p1 = Point(3,4)
p2 = Point(2,3)
print(p1)
print(p1.y)
print(p1+p2) 
print(p1.__sub__(p2))
print(p1.__Mul__(p2))


a = [0, 1, 2, 3] 
print([x*x for x in a if x % 2 == 0])  

i = 1
for i in range(1, 10):
    print(math.sqrt(i))
    i = i + 1
