# from stack import stack
from stack import stack
import math

def modWithTwo(decNum):
    listAngka = stack()
    hasilBagi = decNum
    pembagi = 26
    while hasilBagi > 1:
        # / menghasilkan nilai bulet, bukan koma2
        processNum = hasilBagi
        hasilBagi = hasilBagi/pembagi
        hasilMod = processNum-((hasilBagi)*pembagi)
        listAngka.push(hasilMod)
    listAngka.push(hasilBagi)

    binaryString = ""
    while not listAngka.isEmpty():
        hasil = True
        binaryString = binaryString + str(listAngka.pop())
    return binaryString

    # masukkan angka, di mod dengan 2, simpan hasil mod ke listAngka dengan append
    # keluakan hasilnya dengan pop

print modWithTwo(26)