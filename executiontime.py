
import time

def sumOfN(n):
    start = time.time()
    theSum = 0
    for i in range(1, n+1):
        theSum += i
    end = time.time()
    return theSum, end-start

def sumOfN2(n):
    start = time.time()
    theSum = 0
    for i in range(1, n+1):
        theSum += i

    end = time.time()
    return theSum, end-start

def sumOfN3(n):
    start = time.time()
    theSum = (n*(n+1))/2
    end = time.time()
    return theSum, end-start

for i in range(5):
    print('Sum1 is %d required %10.7f seconds'%sumOfN(100000))
print('\n')

for i in range(5):
    print('Sum2 is %d required %10.7f seconds'%sumOfN2(100000))
print('\n')

for i in range(5):
    print('Sum3 is %d required %10.7f seconds'%sumOfN3(100000))
print('\n')
