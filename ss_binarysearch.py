# prinsipnya adalah divide and conquer
# divide the problem into smaller pieces and
# solve the smaller pieces in some way
# reassemble the whole problem to get the result

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first+last)/2
        # root adalah alist[midpoint]
        if alist[midpoint] == item:
            found = True
        else:
            if item > alist[midpoint]:
                first = midpoint + 1
            else:
                last = midpoint - 1
    return found

# in recursive version
def recBinarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)/2
        # root adalah alist[midpoint]
        if alist[midpoint] == item:
            return True
        else:
            if item > alist[midpoint]:
                # first = midpoint + 1
                return recBinarySearch(alist[midpoint+1:], item)
                # print(alist[midpoint+1:], item)
            else:
                # last = midpoint - 1
                return recBinarySearch(alist[:midpoint], item)
                # print(alist[:midpoint], item)

testlist = [1, 3, 4, 6, 7, 8, 9,11,34, 54,76,90, 23]

# nanti bisa ditambahi mikrosekon execution time
# print binarySearch(testlist, 13)
print recBinarySearch(testlist, 3)

# mengganti suatu program jadi bentuk recursive
# adalah menghilangkan while/looping menjadi recursive/pemanggilan dirinya sendiri