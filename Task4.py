import random

"""
Task4
"""

sizeOfList = 10
List = [1,2,2,4,5,6,7,8,9,10]
"""
for x in range(0,sizeOfList):
    List.append(random.randint(1,1024))
"""
print(List)

for i in range (1, sizeOfList/2):
    for j in range (i, sizeOfList):
        for k in range (i+1, sizeOfList):
            for l in range (k, sizeOfList):
                if (List[i]*List[j])==(List[k]*List[l]) and List[i] != List[j] != List[k] != List[l]:
                    print "{} & {} and {} & {} are a 2-pair".format(List[i],List[j],List[k],List[l])
                