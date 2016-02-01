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

    def isEmpty(self):
        return self.head == None


temp = node(93)
print temp.getData()