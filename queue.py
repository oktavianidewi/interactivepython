class queue:
    def __init__(self):
        self.orang = []

    def isEmpty(self):
        return self.orang == []

    def enqueue(self, item):
        # karena sistemnya FIFO, maka nggak pake append
        # self.orang.append(self, item)
        self.orang.insert(0, item)

    def dequeue(self):
        return self.orang.pop()

    def show(self):
        return self.orang

    def size(self):
        return len(self.orang)

"""
q = queue()
q.enqueue(4)
q.enqueue("dog")
q.enqueue(True)
print(q.size())
print(q.show())
"""