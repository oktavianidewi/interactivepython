# improves the insertion sort by breaking the original list into a number of smaller sublist

def diyShellSort(alist, gap = None):
    # pembagi didapat dari faktor pembagi len(alist)
    # misal, 10 maka fpb nya 2, 5, 1

    # kalo gap ada isinya
    if gap :
        print gap
        diyGap(alist, gap)
    else:
        # kalo gap ga ada isinya, jalankan ini
        i = len(alist)
        hasilBagi = []
        while i > 1:
            i = i // 2
            hasilBagi.append(i)

        for i in hasilBagi:
            print i
            diyGap(alist, i)

    #return hasilBagi

def diyGap(alist, gap):
    # prinsipnya adalah:
    # breakdown and conquer dengan nilai yang ada pada setiap breakdown-an

    for i in range(0, gap, 1):
        # print "   ", i

        if gap == len(alist):
            gap = 1

        # for sampe sejumlah pembagi
        for j in range(i, len(alist), gap):
            # print "      ", j

            for k in range(j+gap, len(alist), gap):
                # print "         ", k

                # j = minPointer
                # k = currentPointer
                if alist[j] > alist[k]:
                    # tukar
                    # ketika nilai alist[j] lebih besar dari alist[k]
                    temp = alist[j]
                    alist[j] = alist[k]
                    alist[k] = temp
    print alist

alist1 = [54, 26, 93, 17, 77, 31, 44, 55, 20, 21]
alist2 = [5, 16, 20, 12, 3, 8, 9, 17, 19, 7]
# diyShellSort(alist2, 3)
diyShellSort(alist2)

# gimana caranya supaya recursive?