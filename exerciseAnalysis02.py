# Devise an experiment to verify that
# get item and set item are O(1) O1 for dictionaries.
# gimana cara menggunakan get item dan set item di dictionary?
# kalo get item hampir sama kayak index di list

'''
dictionary = {'a':1, 'b':2, 'c':3}

for key in dictionary:
    print( dictionary.get(key) )
'''
import timeit
import random

for i in range(10000,100000, 20000):
    # membuat dictionary dengan isi generated from range value
    # melakukan set index
    x = {z:None for z in range((i))}
    # x.get(random.randrange(i))
    set_dict = timeit.Timer("x[(random.randrange(%d))]" %i, "from __main__ import random, x")

    # mendapatkan nilai index / get index
    # jika get dulu baru set, maka nilai index nya None,
    # harus di set dulu dengan random value
    get_dict = timeit.Timer("x.get(random.randrange(%d))" %i , "from __main__ import random, x")

    set_time = set_dict.timeit(number=1000) # apa ya maknanya dari number di timeit ini?
    get_time = get_dict.timeit(number=1000) # apa ya maknanya dari number di timeit ini?

    print("%d \t %10.4f \t %10.4f" %(i, get_time , set_time))