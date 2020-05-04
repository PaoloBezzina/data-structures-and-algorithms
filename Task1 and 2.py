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

"""
Testing Task1
"""

print("\nBefore sort Array A of size:")
print(arrA)

shellSort(arrA)

print("\nAfter sort Array A")
print(arrA)

print("\nBefore sort Array B")
print(arrB)

quickSort(arrB, 0, (len(arrB)-1))

print("\nAfter sort Array B")
print(arrB)


"""
Task 2
"""

#Using Merge function from Merge Sort

def mergeArrays(arr1, arr2):

    size_Arr1 = len(arr1)
    size_Arr2 = len(arr2)

    size_Arr3 = size_Arr1 + size_Arr2
    arr3 = [0] * size_Arr3
    i,j,k = 0,0,0

    while i < size_Arr1 and j < size_Arr2: 

        #check elements of both arrays, storing smallest element in both arrays at current position
        if arr1[i] < arr2[j]: 
            arr3[k] = arr1[i] 
            k = k + 1
            i = i + 1
        else:
            arr3[k] = arr2[j] 
            k = k + 1
            j = j + 1

    # Store all other elements

    #from first array
    while i < size_Arr1: 
        arr3[k] = arr1[i]; 
        k = k + 1
        i = i + 1

    #from second array
    while j < size_Arr2: 
        arr3[k] = arr2[j]; 
        k = k + 1
        j = j + 1

    print("\nMerged arrays A and B")
    print(arr3)

mergeArrays(arrA, arrB);


