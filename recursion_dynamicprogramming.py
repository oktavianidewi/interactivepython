def recMC(coinValueList, change):
    """
def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1+recMC(coinValueList, change-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

"""

    for i in [c for c in coinValueList if c <= change]:
        print i
        numCoins = recMC(coinValueList, change-i)
        print numCoins


print recMC([1,5,10,25], 20)
print recMC([1,5,10,25], 100)