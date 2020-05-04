 
def checkRepeatedM1(arr): 

    size = len(arr)

    for i in range (0, size): 
            for j in range (i + 1, size): 
                if arr[i] == arr[j]: 
                    print(arr[i], end = " ")
    print(" ")


def checkRepeatedM2(arr):
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


array1 = [1,2,2,3,4,5,6,7,7,8,9,7,10,2,7,2,8]
array2 = [10,9,8,7,6,5,4,3,2,1]

checkRepeatedM2(array1)
checkRepeatedM2(array2)