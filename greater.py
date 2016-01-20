#compare number in list, find the biggest one
import time
from random import randrange

def findMin(alist):
    # #kenapa kok butuh mendefinisikan ini? biasa, untuk default variabel aja
    overallmin = alist[0]
    for i in alist:
        issmallest = True
        for j in alist:
            if i != j:
                if i > j:
                    issmallest = False
                #print i,'vs',j
        if issmallest:
            overallmin = i

    return overallmin

def findMinSoFar(alist):
    # #kenapa kok butuh mendefinisikan ini? biasa, untuk default variabel aja
    minSoFar = alist[0]
    for i in alist:
        if i < minSoFar:
            minSoFar = i
    return minSoFar

# print(findMin([9, 3, 6, 7, 8, 10]))
# print(findMinSoFar([9, 3, 6, 7, 8, 10]))

# why nsquare? perhatikan loop n nya,
# atau coba cek berapa time yang di-spend dengan program berikut:

for listSize in range(1000, 10001, 1000):
    # nilai alist isinya random number 0-100000, lebar array awalnya 1000 di tiap iterasi nambah 1000 terus sampe iterasi ke-10 dan nilai maksimal 10.001
    # membuat array dengan size 1000 dan sampe 10001, dengan rentang 1000
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(findMinSoFar(alist))
    end = time.time()
    print('size: %d time: %f' %(listSize, end-start))
    # resultnya adalah nilai paling rendah dari nilai random di array dan waktu eksekusi masing2 array
    # makin banyak jumlah array yang diproses, makin besar waktu yang dibutuhkan besaran running time sesuai logaritmik algorithm

    '''
    hasil execute time findmin
    7
    size: 1000 time: 0.133832
    74
    size: 2000 time: 0.560918
    23
    size: 3000 time: 1.278232
    28
    size: 4000 time: 2.129658
    5
    size: 5000 time: 3.552552
    17
    size: 6000 time: 5.120262
    17
    size: 7000 time: 6.801660
    4
    size: 8000 time: 12.912355
    3
    size: 9000 time: 11.995822
    3
    size: 10000 time: 13.832411

    Process finished with exit code 0

    -------
    hasil execute time findminsofar

    5
    size: 1000 time: 0.000049
    54
    size: 2000 time: 0.000070
    188
    size: 3000 time: 0.000118
    85
    size: 4000 time: 0.000174
    21
    size: 5000 time: 0.000167
    8
    size: 6000 time: 0.000199
    14
    size: 7000 time: 0.000250
    18
    size: 8000 time: 0.000426
    13
    size: 9000 time: 0.000306
    6
    size: 10000 time: 0.000374


    '''