# dari file queue.py import class queue
from queue import queue
# from pythonds.basic.queue import Queue

def hotpotato(namelist, num):
    simqueue = queue()
    # simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        print "ke-%d" %simqueue.size()
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
            print i, ": ", simqueue.show()
        simqueue.dequeue()
    quit()
    #   return simqueue.dequeue()

#print(hotpotato(["hermione", "harry", "ron", "ginny", "neville", "fred", "george", "bill"], 10))
print(hotpotato(["Bill","David","Susan","Jane","Kent","Brad"],6))