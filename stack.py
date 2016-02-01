class stack:
    def __init__(self):
        self.rak = []

    def push(self, item):
        self.rak.append(item)

    def pop(self):
        return self.rak.pop()

    def isEmpty(self):
        return self.rak == []

    def peek(self):
        return self.rak[len(self.rak)-1]

    def size(self):
        return len(self.rak)

    def show(self):
        return self.rak


'''
s = stack()
print(s.isEmpty())
s.push(4)
s.push("dog")
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
'''