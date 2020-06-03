"""
Task 12
"""

def fibonacci(n):

    if n<=0:
        return 0

    list = [0]* (n+1)

    list[0] = 1
    list[1] = 1
    
    sum = 1

    for i in range(2, n+1):
        list[i] = list[i-1] + list[i-2]

    
    for j in range(0, n):
        print(list[j])
        sum += list[j]

    return sum

"""
Testing Task 12
"""

num = 10
print ("\nSum = ", fibonacci(num))