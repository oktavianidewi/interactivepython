def binaryTree(r):
    return [r, [], []]

def insertLeft(root, newBranch):
    # pop ini untuk mengeluarkan/menghapus nilai elemen sesuai nilai index
    # if no index is specified, pop removes the last item in the list
    print("isi dari root sebelum di-pop : ", root)
    t = root.pop(1)
    # kalo pake t = root[1], hasil root-left : [3, [5, [4, [], []], []], []]
    # t = root[1]
    # kalo pake t = root[1], hasil root-left : [3, [5, [4, [], []], []], [4, [], []], [], []]
    # kenapa kok ada node 4 lagi dibelakangnya? aneh

    # pop(1) untuk mengeluarkan node left pertama
    # kalo dikosongi, akan mengeluarkan node right
    # kenapa kok harus di-pop? untuk bisa diukur lebarnya,
    # kalo node tsb ada isinya, maka isikan ke child node. kalo node masih kosong, maka isikan ke node tersebut
    print(newBranch, " - ", t, " dengan lebar ", len(t))
    if len(t) > 1:
        # beda insert dan append. kalo append selalu nambahin di akhir,
        # kalo insert (defaultnya) selalu nambahkan di awal, tapi bisa diubah sesuai nilai index
        # tiap ada data baru yang masuk, selalu dijadikan parent dari child.
        # node baru mengisi 1 tingkat diatas node yg udah ada
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    print("\n")
    return root
def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    print("\n")
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = binaryTree(3)
insertLeft(r, 4)
insertLeft(r, 5)
insertRight(r, 6)
insertRight(r, 7)
l = getLeftChild(r)
print(r)

setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))

a = binaryTree('a')
insertLeft(a, 'b')
insertRight(a, 'c')
insertRight(getLeftChild(a), 'd')
insertLeft(getRightChild(a), 'e')
insertRight(getRightChild(a), 'f')
print(a)