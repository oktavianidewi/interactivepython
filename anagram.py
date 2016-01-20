# mendeteksi 2 kata apakah anagram dari kata tertentu
# belum bisa mendateksi anagram yang dipisah spasi dan beda besar-kecilnya huruf
# tes aku tambahin komen
def anagramSolution(s1, s2):
    # mengubah s2 kedalam bentuk list array
    alist = list(s2)
    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1
        if found:
            alist[pos2] = None
        else:
            stillOK = False
        pos1 += 1
    return stillOK

# anagram ini bisa juga diselesaikan dengan sorting, metode sorting ini kayak bag of words.
# ngga memperhatikan urutan dalam kalimat

def anagramSolution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if(alist1[pos] == alist2[pos]):
            pos += 1
        else:
            matches = False
    return matches

# solusi selanjutnya adalah dengan komputasi jumlah huruf yang sama pada kalimat tersebut.
# ini masuk akal juga,

def anagramSolution4(s1, s2):
    # space alfabet ada 26
    c1 = [0]*26
    c2 = [0]*26

    # fungsi ord untuk represent an integer unicode character, misal ord('a') = 97
    # tapi kenapa kok dikurangi a semua ya? sebagai pemersatu, supaya bisa berada di array karakter yang sama
    # mengisi array c1
    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] += 1

    # mengisi array c2
    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] += 1

    # membandingkan isi array c1 dan c2, kalau semua array valuenya sama -> anagram detected
    j = 0
    stillOK = True
    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j += 1
        else:
            stillOK = False
    return stillOK

print(anagramSolution4('iamlordvoldemort', 'tommarvoloriddle'))