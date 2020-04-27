 
def checkRepeatedM1(arr): 

    size = len(arr)

    for i in range (0, size): 
            for j in range (i + 1, size): 
                if arr[i] == arr[j]: 
                    print(arr[i], end = " ")
    print(" ")

"""
def checkRepeatedM2(arr):
    size = len(arr)

    for i in range(0, size):
        x = arr[i]
        if x in arr:
            print(x, end = " ")
    print(" ")
"""

array1 = [1,2,2,3,4,5,6,7,7,8,9,7,10]
array2 = [10,9,8,7,6,5,4,3,2,1]

checkRepeatedM1(array1)
checkRepeatedM1(array2)