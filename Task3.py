"""
Task 3
"""

#A = [0, 5, 3, 6, 8, 7, 15, 9]
A = [10, 20, 30, 40, 50, 60, 70, 80, 90]
n = len(A)
Extreme = []

for i in range(0,n):
    if (0 < i < n-1) and ((A[i-1] < A[i] > A[i+1]) or (A[i-1] > A[i] < A[i+1])):
        Extreme.append(A[i])


if(Extreme == []):
    print("SORTED")
else:
    print("Extreme Elements:")
    print(Extreme)

"""
If an array is sorted the A[i] element will always be larger than the previous value(A[i-1]) and smaller the the next value(A[i+1]).
Therefore. by skipping the first and last elements of the array,since these cannot have smaller or larger elements, you will never end up with extreme values.
"""