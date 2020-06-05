def checkRepeated(arr):
    size = len(arr)
    repeated = []

    for i in range (0, size):
            for j in range (i + 1, size): 
                if arr[i] == arr[j]: 
                    if arr[i] in repeated:
                        continue
                    else:
                        repeated.append(arr[i])
    print(repeated)

"""
Testing Task 9
"""

array1 = [10,9,8,7,6,5,4,3,2,1]
array2 = [1,2,2,3,4,5,6,7,7,8,9,7,10,2,7,2,8]

checkRepeated(array1)
checkRepeated(array2)