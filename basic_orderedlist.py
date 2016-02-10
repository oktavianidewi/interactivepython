# implementng unordered list, urut descending atau ascending
class node:
    def __init__(self, newItem):
        self.data = newItem
        self.selanjutnya = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.selanjutnya

    def setData(self, newItem):
        self.data = newItem

    def setNext(self, newItem):
        self.selanjutnya = newItem

class orderedlist:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        hopNumber = 0
        while current != None:
            hopNumber += 1
            current = current.getNext()

        return hopNumber

    def tambah(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def add1(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head == temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def remove(self, item):
        pass

    def search(self, item):
        pass

mylist = orderedlist()

'''
mylist.tambah(1)
mylist.tambah(2)
mylist.tambah(3)
mylist.tambah(4)
mylist.tambah(5)
mylist.tambah(6)
'''
mylist.add1(1)
mylist.add1(2)
mylist.add1(3)
mylist.add1(4)
mylist.add1(5)
mylist.add1(6)

print(mylist.isEmpty())
print(mylist.size())