"""
Task 3
"""

A =  [0, 5, 3, 6, 8, 7, 15, 9]  
n = len(A)
A_Extreme = []

for i in range(0,n):
    if (0 < i < n-1) and ((A[i-1] < A[i] > A[i+1]) or (A[i-1] > A[i] < A[i+1])):
        A_Extreme.append(A[i])


if(A_Extreme == []):
    print("SORTED")
else:
    print(A_Extreme)

"""

"""