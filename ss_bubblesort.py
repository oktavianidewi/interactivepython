def diyBubbleSort(alist):
    for iterasiEksternal in reversed(range(len(alist))):
        print iterasiEksternal
        for nilaiInternal in range(iterasiEksternal):
            if alist[nilaiInternal] > alist[nilaiInternal+1]:
                temp = alist[nilaiInternal]
                alist[nilaiInternal] = alist[nilaiInternal+1]
                alist[nilaiInternal+1] = temp
            print alist

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
blist = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]

# bubbleSort(blist)
diyBubbleSort(blist)
# print alist