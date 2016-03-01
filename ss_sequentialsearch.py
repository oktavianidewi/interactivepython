def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found

def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    alist.sort()

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] >item:
                stop = True
            else:
                pos = pos + 1
    return found

testlist = [1, 3, 4, 6, 7, 8, 9,11,34, 54,76,90, 23]

# nanti bisa ditambahi mikrosekon execution time
print sequentialSearch(testlist, 13)
print orderedSequentialSearch(testlist, 13)