from deque import deque

def palindromeChecker(words):
    wordque1 = deque()
    equal = True

    for i in words:
        wordque1.addRear(i)

    while wordque1.size() > 1 and equal:
        first = wordque1.removeFront()
        last = wordque1.removeRear()
        if first != last:
            equal = False

    return equal

print palindromeChecker("radar")