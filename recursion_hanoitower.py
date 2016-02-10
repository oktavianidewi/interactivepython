def moveDisk(fp, tp):
    print("moving disk from ", fp, "to", tp)

def moveTower(height, a, b, c):
    if height >= 1:
        moveTower(height-1, a, c, b)
        moveDisk(a, c)
        moveTower(height-1, b, a, c)

moveTower(5, "A", "B", "C")