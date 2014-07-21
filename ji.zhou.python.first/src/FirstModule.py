'''
Created on 18 Jul 2014

@author: Ji Zhou Gash
'''

from random import randint

def add(a,b):
    return a+b

def addFixedValue(a):
    y = 5
    return y + a

def readList(c):
    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if c>=len(myList):
        ramNo = randint(0, len(myList))
    else:
        ramNo = randint(0, c)
        
    for element in myList:
        print(element)     
        
    return myList[ramNo]

# The main class
FullName = "Ji Zhou"
x = 1 
y = 4 
z = x + y

print(z <= x)
print(add(1,2))
print(addFixedValue(1)) 

assert(len(FullName) > 1) 

i = 1
for i in range(0, len(FullName)-1):
    
    if i <= len(FullName)/2:
        print(FullName[i] + "\t") 
    else:
        print(FullName[-i] + "\t")

print("abcdefg"[0:4])        
print('x' + str(y) + 'z') 


number = FullName
try:
    value = int(number)
except ValueError:
    value = 'NAN'

print(value + str(len(value)))

# print(readList(5))

lotterNo = "abc"
try: 
    lotterNo = int(number)
except ValueError:
    lotterNo = z
    
print("The number you get is: " + str(readList(lotterNo)))
    