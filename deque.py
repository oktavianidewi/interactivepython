class deque:
    def __init__(self):
        self.antrian = []

    def addFront(self, item):
        self.antrian.insert(0, item)
        
    def addRear(self, item):
        # self.antrian.append(item)
        self.antrian.insert(len(self.antrian), item)
        # self.antrian.append(item) # append = insert(nilai maks, item)

    def removeFront(self):
        self.antrian.pop()

    def removeRear(self):
        self.antrian.pop(0)

    def isEmpty(self):
        return self.antrian == []

    def size(self):
        return len(self.antrian)

    def show(self):
        print self.antrian
"""
d=deque()
print(d.isEmpty())
#d.addRear(4)
#d.addRear('dog')
#d.addRear(8.4)

d.addFront('cat')
d.addFront(True)
print(d.size())
print(d.isEmpty())
#print(d.removeRear())
#print(d.removeFront())
d.show()
"""