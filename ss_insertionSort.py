def diyInsertionSort(alist):
    for i in range(0, len(alist)-1, 1):
        currentPos = i
        for j in reversed(range(len(alist[:i]))):
            print "nilai j : ", j
            print alist[currentPos], ">", alist[j]
            print "posisi :", currentPos, ">", j
            if alist[currentPos] < alist[j]:
                # shift position
                temp = alist[currentPos] # 4
                alist[currentPos] = alist[j] # 7
                alist[j] = temp #4
                currentPos = j
            print alist
        print "\n"
        print alist

alist = [15, 5, 4, 18, 12, 19, 14, 10, 8, 20]
diyInsertionSort(alist)

'''
contoh insertion sort
[3] 7   4   9   5   2   6   1
(3) [7] 4   9   5   2   6   1
3   (7) [4] 9   5   2   6   1
3   (4) 7   [9] 5   2   6   1
3   4   7   (9) [5] 2   6   1
3   4   (5) 7   9   [2] 6   1
(2) 3   4   5   7   9   [6] 1
2   3   4   5   (6) 7   9   [1]
(1) 2   3   4   5   6   7   9

goal :  1    2   3   4   5   6   7   9
[] currentPos menunjukkan urutan angka yang akan di-sort
()
bukan men-swap tapi memindahkan. contoh, saat membandingkan angka 5
angka 5 ngga di-swap dengan 7 tapi, angka 7 dan 9 di-geser/shift

bedanya dengan selectionSort adalah, ada currentPos yang berubah
'''