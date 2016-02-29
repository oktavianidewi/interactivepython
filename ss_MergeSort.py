# divide and conquer
# recursive algorithm that continuously splits a list in half
# first: the list is splitted into halves
# second :
# second: process in the merge

# kunci dari recursive adalah: kerjakan dengan input yang paling kecil
# kalau berhasil, baru diulang ke input yang lebih besar

# non-recursive merge sort

hasil = []
def recursivebagi(x):
    hasil.append(x)
    x = x // 2

    if x > 1:
        recursivebagi(x)

    return hasil

# recursivebagi(20)

def diyMergeSort(alist):
    division = recursivebagi(len(alist))
    # print division
    for i in reversed(range(len(division))):
        print division[i]

        start = 0
        gap = division[i]
        for j in range(start, len(alist), gap):
            print "   ", j
            for k in range(j,j+gap-1, 1):
                print "      ", k
                for l in range(k+1, j+gap, 1):
                    # if k < (j+gap)-1:
                    print "      ", alist[k], " > ", alist[l]
                    if alist[k] > alist[l]:
                        # print "      tukar"
                        temp = alist[k]
                        alist[k] = alist[l]
                        alist[l] = temp
                        print "      ", alist
            # start += finish
            # finish += finish
    print alist

alist = [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]
diyMergeSort(alist)


'''
# recursive mergesort
def diyMergeSort(alist):
    mid = len(alist)/2
    left = alist[:mid]
    right = alist[mid:]

    # print mid print left
    # if mid > 1: mid = mid - 1

    if mid > 1:
        diyMergeSort(left)
        diyMergeSort(right)


    # print alist
    print left
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        print left[i] , " > ", right[j]
        if left[i] > right[j]:
            alist[k] = right[j]
            j += 1
        else:
            alist[k] = left[i]
            i += 1
        k += 1

    while i < len(left):
        print left[i]
        alist[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        print right[j]
        alist[k] = right[j]
        j += 1
        k += 1

    print alist
    # quit()
    # untuk mengurutkan left dan right, step nya sama, sehingga lebih baik di rekursi
'''