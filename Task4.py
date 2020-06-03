"""
Task4
"""

#List = [1,3,2,4,5,6,7,8,9,10]
#List = [1,2,2,3,4,5,2,6,7,8,9,10]
List = [1,1024,2,512,4,80,23,999,456,739,3,200,100]

sizeOfList = len(List)

print(List)

for i in range (1, int(sizeOfList/2)):
    for j in range (i, sizeOfList):
        for k in range (i+1, sizeOfList):
            for l in range (k, sizeOfList):
                if (List[i]*List[j])==(List[k]*List[l]) and List[i] != List[j] != List[k] != List[l]:
                    print ("{} & {} and {} & {} are a 2-pair".format(List[i],List[j],List[k],List[l]))
                