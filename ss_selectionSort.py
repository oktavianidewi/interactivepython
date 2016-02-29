def diySelectionSort(alist):
    # yang udah di-swap ngga usah dibandingkan lagi,
    # urutkan dari kecil ke besar
    # goalnya : [17,20,26,31,44,54,55,77,93]

    for i in reversed(range(len(alist))):
        pointerOfMin = 0
        for j in range(i):
            print alist[pointerOfMin], " < ", alist[j+1], ":", alist[pointerOfMin] < alist[j+1]
            if alist[pointerOfMin] > alist[j+1]:
                pointerOfMin = pointerOfMin
            else:
                pointerOfMin = j + 1
            # perintah end hanya bisa di execute di python 3.5 print(alist[j], end="\t") print("\n")
            print "   ",alist


        # mau tuker 17 dan 20
        temp = alist[pointerOfMin] #17
        alist[pointerOfMin] = alist[j+1]
        alist[j+1] = temp

        print "\n"

alist = [54,26,93,17,77,31,44,55,20]
# alist = [11, 7, 12, 14, 19, 1, 6, 18, 8, 20]

# selectionSort(alist)
diySelectionSort(alist)
