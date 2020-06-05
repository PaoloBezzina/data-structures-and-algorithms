"""
Task 11
**  = 'to the power of'
Maclaurin's Expantion
"""
import math

def cos(x, n):
    cos = 0
    for n in range(n):
        cos = cos + ((-1)**n) * (x ** (2*n)) / (math.factorial(2 * n))
    return cos

def sin(x,n):
    sin = 0
    
    for n in range(n):
        sin = sin + ((-1)**n) * (x ** ((2*n)+1)) / math.factorial((2*n)+1)
    return sin

"""
Testing Task 11
"""

terms = 25
print("Cos:")
print (cos(1.2, terms))
print("\nSin:")
print (sin(1.2, terms))