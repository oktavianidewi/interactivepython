def diyQuickSort(alist):
    if len(alist) > 1:
        print "lebar : ", len(alist)
        pivot = alist[0]
        smallerAlist = []
        greaterAlist = []
        equalAlist = []
        # print len(alist)
        for i in range(0, len(alist), 1):
            # print i
            print pivot , ">", alist[i]
            if pivot > alist[i]:
                smallerAlist += [alist[i]]
            if pivot == alist[i]:
                equalAlist += [alist[i]]
            if pivot < alist[i]:
                greaterAlist += [alist[i]]

            print smallerAlist
            print equalAlist
            print greaterAlist
            newlist = diyQuickSort(smallerAlist)+equalAlist+diyQuickSort(greaterAlist)
        return newlist
    else:
        return alist
        # print "newalist ", newalist

# alist = [54,26,93,17,77,31,44,55,20]
alist =  [14, 17, 13, 15, 19, 10, 3, 16, 9, 12]
print diyQuickSort(alist)
# print sort(alist)
