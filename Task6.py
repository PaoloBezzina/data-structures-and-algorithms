"""
Task 6

Explain Optimisations: 
"""

def sieveOferatosthenes(num):
    #initialising all elements in the array as true meaning prime
    primeNumbers = [True] * (num+1)

    testFor = 2

    while (testFor*testFor <= num):

        if (primeNumbers[testFor] == True):

            for i in range(testFor * testFor, num + 1, testFor): 
                primeNumbers[i] = False

        testFor = testFor + 1

    for int in range(2, num): 
        if primeNumbers[int]: 
            print (int), 


def checkPrime(num):

    prime = bool(False)

    #if number is less than 1 it cannot be prime
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                #not a prime number
                break
        else:
            prime = bool(True)

    return prime 



toTest = int(input("Input number to check if prime: "))
if checkPrime(toTest) is True:
    print (toTest, (" is a prime number"))
else:
    print (toTest, (" is not prime number"))

sieveOferatosthenes(30)