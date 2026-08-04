from functools import reduce

l=[1,2,3,4,5,6]
'''Wroking of Reduce func.
   [3,3,4,5,6]
   [6,4,5,6]
   [10,5,6]
   [15,6]
   [21]
'''

def sum(a,b):
    return a+b

c=reduce(sum,l)
print(c)