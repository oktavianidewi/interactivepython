import timeit
import random

# generate nilai i dari 10.000, 30.000, 50.000, 70.000, 90.000
for i in range(10000, 1000001, 20000):
    t = timeit.Timer("random.randrange(%d) in x"%i, "from __main__ import random, x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)

    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print('%d, %10.3f, %10.3f' %(i, lst_time, d_time))


    '''
    untuk mengetahui nilai big o juga bisa pake plot

    import matplotlib.pyplot as plt

    def f2(L):
        sum = 0
        i = 1
        times = 0
        while i < len(L):
            sum = sum + L[i]
            i = i * 2
            times += 1    # track how many times the loop gets called
        return times

    def main():
        i = range(1200)
        f_i = [f2([1]*n) for n in i]
        plt.plot(i, f_i)

    if __name__=="__main__":
        main()

    '''