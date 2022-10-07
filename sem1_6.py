#Дана функция log()

from math import *
import matplotlib.pyplot as plt
import numpy as np
#global EPS
global count
#EPS = 1
count = 0
def show():
    fig = plt.figure(figsize=(8, 2.5), facecolor="#f1f1f1")
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8  # задаем значения переменных
    ax = fig.add_axes((left, bottom, width, height))

    x1 = np.linspace(-10, 10, 1000)
    x2 = np.array([log10(0.000001),log10(1),log10(2),log10(3),log10(4),log10(5),log10(6),log10(7),log10(8),log10(9),log10(10)])
    y1 = np.log10(x1)
    y2 = np.log10(x2)
    #ax.plot(x1, y1)
    #ax.plot(x2, y2)
    x = np.arange(-10, 10.01, 0.01)
    plt.plot([0.000001,1,2,3,4,5,6,7,8,9,10],[log10(0.000001),log10(1),log10(2),log10(3),log10(4),log10(5),log10(6),log10(7),log10(8),log10(9),log10(10)])
    plt.plot(x,np.log10(x))
    #ax.set_xlabel("x")
    #ax.set_ylabel("y")

    plt.show()
    #fig.savefig("1a.png", dpi=100, facecolor="#f1f1f1")

def prog(EPS):
    max_d = 1000000
    while max_d > 0.0000001:
        print("max_d=",max_d)
        if(max_delt(EPS, max_d)<max_d):
            print("<>")
            max_d = max_delt(EPS, max_d)
        EPS /= 10
    return 10/EPS
def polinom1(x, x0, x1):
    return log10(x0) + (log10(x1)-log10(x0))*(x - x0)/(x1 - x0)
def max_delt(EPS, md):
    res = 0
    #count = 0
    x0 = 1e-100
    x1 = x0+EPS
    while x1<10:
        if(delt(x0,x1)>res):
            res = delt(x0,x1)
        x0 = x1
        x1 = x0 + EPS
        #count += 1
   # print(count)
    #if(x1>10):
     #   res = md
    return res

def delt(x0, x1):
    res = 0
    EPS1=1e-6
    #print(res)
    x = x0
    while x < x1:
        d = abs(polinom1(x,x0,x1)-log10(x))
        if(d>res):
            res = d
        x+=EPS1
    print("res=",res)
    return res

if __name__ == '__main__':
    print(prog(1))
    #show()