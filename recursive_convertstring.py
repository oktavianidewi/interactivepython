import math
from stack import stack

# without stack
def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n % base]

# with stack
rStack = stack()
def toStrStack(n, base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n//base
    res = ""

    # ketika tidak kosong
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res

# print(toStr(1453, 6))
print(toStrStack(1453, 6))