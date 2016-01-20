# Devise an experiment to verify that
# the list index operator is O(1)
# maksudnya gimana sih? keywordnya: LIST, INDEX OPERATOR
# apakah pada LIST ada operator INDEX?
# buat simulasi dengan waktu butuh timeit
# dan apa yang diukur? waktu yang dibutuhkan untuk mendapatkan index

import timeit
import random

'''
word = 'apple'
lword = list(word)
print(lword.index('p'))
'''

j = 10
for i in range(10000,100000, 20000):
    # membuat list dengan isi generated from range value
    x = list(range(i))
    # t = timeit.Timer( "x.index(random.randrange(%d))" %i, "from __main__ import random, x" )
    # t = timeit.Timer( "x.pop(random.randrange(%d))" %i, "from __main__ import random, x" )
    t = timeit.Timer( "del x[random.randrange(%d)]" %j, "from __main__ import random, x" )
    '''
    The time increases as the i value increases because this code uses the list.index(x) method instead of the list index operator list[x].
    The list.index(x) method searches linearly through a list until it finds the item x, then it returns the index of that item. If list.index(x) doesn't find an item x, then it returns an error.
    The list index operator list[x] returns an item at index x of the list, and runs in constant time.
    Below is a solution that yields time complexity of O(1):
    '''
    indextime = t.timeit(number=1000)
    print("%d \t %10.4f" %(i, indextime))
    #print( 'Iterasi ke-%d : index yang ditermukan %d' % (i, x.index(random.randrange(i))) )
