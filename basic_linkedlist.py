class node:
    def __init__(self, initdata):
        # kalau self.head = None -> there is no nodes in the linked list
        self.head = None
        self.data = initdata

        # kalau self.next = None -> node tersebut adalah node terakhir
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class unorderedlist:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = node(item)
        # menyimpan info pointer selanjutnya adalah old head
        temp.setNext(self.head)
        #  mengisi nilai head baru dengan nilai item
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current!=None:
            count += 1
            current = current.getNext()
        return count

    def search(self, keyword):
        current = self.head
        count = 0
        found = False
        while found == False and current != None:
            if current.getData() == keyword:
                found = True
            else:
                count += 1
                current = current.getNext()
        return found

    def remove(self, keyword):
        current = self.head
        count = 0
        found = False
        while found == False:
            if current.getData() == keyword:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext
        else:
            previous.setNext(current.getNext())

mylist = unorderedlist()
mylist.add(0)
mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.add(5)
print(mylist.size())
print(mylist.search(2))
print(mylist.remove(4))
print(mylist.size())
