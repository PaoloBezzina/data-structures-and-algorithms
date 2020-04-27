import random

"""
Task 1

"""

def shellSort(arr): 
  
    n = len(arr) 
    gap = n//2
  
    while gap > 0: 
  
        for i in range(gap,n): 
  
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = arr[i] 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
  
            # put temp (the original a[i]) in its correct location 
            arr[j] = temp 
        gap //= 2

def partition(arr,start,end): 
	i = start-1
	pivot = arr[end]

	for j in range(start, end): 

		if arr[j] <= pivot: 

			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[end] = arr[end],arr[i+1] 
	return i+1

def quickSort(arr,start,end): 
	if start < end: 

        #part is the location of the partition
		part = partition(arr,start,end) 

		quickSort(arr, start, part-1) 
		quickSort(arr, part+1, end) 


arr_Size = []
maxArrSize = 275;

for x in range(2):
    rand = random.randint(256,maxArrSize)

    if(rand in arr_Size):
        #in the case of a duplicate array size, the system simply adds 1 to the size of the second array, making them unequal
        rand = rand + 1
        arr_Size.append(rand)
    else:
        arr_Size.append(rand)

print(arr_Size)

size_ArrA = arr_Size[0]
size_ArrB = arr_Size[1]

arrA = []
arrB = []

for x in range(0,size_ArrA):
    arrA.append(random.randint(0,1024))

for x in range(0,size_ArrB):
    arrB.append(random.randint(0,1024))

print("\nBefore sort Array A of size:")
print(arrA)

shellSort(arrA)

print("\nAfter sort Array A")
print(arrA)

print("\nBefore sort Array B of size:")
print(arrB)

quickSort(arrB, 0, (len(arrB)-1))

print("\nAfter sort Array B")
print(arrB)


"""
Task 2
"""

#Using Merge function from Merge Sort

def mergeArrays(arrA, arrB, size_ArrA, size_ArrB):

    size_ArrC = size_ArrA + size_ArrB
    arrC = []
    i,j,k = 0,0,0

    while i < size_ArrA and j < size_ArrB: 

        #check elements of both arrays, storing smallest element in both arrays at current position
        if arrA[i] < arrB[j]: 
            arrC[k] = arrA[i] 
            k = k + 1
            i = i + 1
        else: 
            arrC[k] = arrB[j] 
            k = k + 1
            j = j + 1

    # Store all other elements

    #from first array
    while i < arrA: 
        arrC[k] = arrA[i]; 
        k = k + 1
        i = i + 1

    #from second array
    while j < arrB: 
        arrC[k] = arrB[j]; 
        k = k + 1
        j = j + 1

arrA = [1, 3, 5, 7] 
n1 = len(arrA) 

arrZ = [2, 4, 6, 8] 
n2 = len(arrZ) 
mergeArrays(arrA, arrB, n1, n2); 