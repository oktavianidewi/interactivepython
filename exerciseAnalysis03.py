# Devise an experiment that
# compares the performance of the del operator on lists and dictionaries.

import random
import timeit

j = 10
for i in range(10000,100000,20000):
    # list

    xlist = list(range(i))
    t = timeit.Timer( "del xlist[random.randrange(%d)]" %j, "from __main__ import random, xlist" )
    list_time = t.timeit(number=1000)

    # x = {z:random.randrange(i) for z in range((i))}
    x = list(range(i))
    tim = timeit.Timer( "del x[random.randrange(%d)]" %j, "from __main__ import random, x")
    tim_time = tim.timeit(number=1000)

    print("%d \t %10.4f \t %10.4f" %(i, tim_time, list_time))