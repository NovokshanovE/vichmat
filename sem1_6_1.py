#Дана функция log()

from math import *
import matplotlib.pyplot as plt
import numpy as np
#global EPS
#global count
#EPS = 1
#count = 0
def show():
    fig = plt.figure(figsize=(8, 2.5), facecolor="#f1f1f1")
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8  # задаем значения переменных
    ax = fig.add_axes((left, bottom, width, height))

    x = np.linspace(0, 10, 1000)

    y = np.log10(x)

    ax.plot(x, y)
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    plt.show()
    #fig.savefig("1a.png", dpi=100, facecolor="#f1f1f1")

def prog(EPS, max_d):
    #global EPS

    if max_d < 1e-6:
        print(max_d)
        return 10/EPS
    if(max_delt(EPS)<max_d):
        max_d = max_delt(EPS)
        print(EPS)
        prog(EPS/10,max_d)

def polinom1(x, x0, x1):
    return log10(x0) + (log10(x1)-log10(x0))*(x - x0)/(x1 - x0)
def max_delt(EPS):
    #global EPS
    #global count
    res = 0
    #count = 0
    x0 = 0.001
    x1 = x0+EPS
    while x1<10:
        if(delt(x0,x1, EPS)>res):
            res = delt(x0,x1, EPS)
        x0 = x1
        x1 = x0 + EPS
        #count += 1
    #print(count)
    return res

def delt(x0, x1, EPS):
    res = 0
    x = x0
    while x < x1:
        d = abs(polinom1(x,x0,x1)-log10(x))
        if(d>res):
            res = d
        x+=EPS
    return res

if __name__ == '__main__':
    print(prog(1, 100))