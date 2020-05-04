"""
Task 10

1: is like a shallow copied list of all elements starting from index 1
"""

def largest(list):
    if len(list) == 1:
        return list[0]
    else:
        m = largest(list[1:])

        if m > list[0]:
            return m  
        else:
            return list[0]
         
a = [1,2,3,4,5,8,2,1,]
print(largest(a))
