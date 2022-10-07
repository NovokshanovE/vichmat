import random
import matplotlib.pyplot as plt
import numpy as np

from base_1 import *

n = random.randint(7,15)
m = random.randint(7,15)
j = [random.randint(0,1000)/1000 for i in range(0, m+1)]
k = [random.randint(0,1000)/1000 for i in range(0, n+1)]



def func_random(x):
    a = []
    b = []
    for i in range(0, m+1):
        a.append(j[i]*x**i)
    for i in range(0, n+1):
        b.append(k[i]*x**i)
    A = np.array(a)
    B = np.array(b)
    return np.sum(A)/(1+abs(np.sum(B)))
def x_y_nodes():
    x_plt = np.linspace(-1, 1, 100)
    y_plt = []
    y_node = []
    x_node = []
    counter = 0
    for i in x_plt:
        y = func_random(i)
        y_plt.append(y)
        if(counter%10==0):
            x_node.append(i)
            y_node.append(y)
        counter += 1
    x_node.append(i)
    y_node.append(y)
    return x_plt, y_plt, x_node, y_node
def f(x):
    return 1. / (1. + 25 * x ** 2)
def advanced_part_tsk_1():
    #f = lambda x: 1. / (1. + 25 * x ** 2)
    N = 11
    #x_node = np.linspace(-1, 1, n)
    #y_node = f(x_node)
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    # определение точек f(x)
    x_plt, y_plt, x_node, y_node = x_y_nodes()

    ax.plot(x_plt, [L(i, np.array(x_node), np.array(y_node)) for i in np.array(x_plt)], 'blue')

    ax.plot(x_node, y_node, 'ro', markersize=10)
    ax.plot(x_plt, y_plt, 'grey')
    ax.grid()
    plt.show()
def advanced_part_tsk_2():
    N = 11
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    x_plt, y_plt, x_node, y_node = x_y_nodes()
    x_chebishev = np.array([np.cos((2*i-1)/(2*N)*np.pi) for i in range(1, N+1)])

    y_chebishev = np.array([func_random(i) for i in x_chebishev])
   # x_plt = np.r_[x_chebishev, x_plt]
    ax.plot(x_plt, [L(i,x_chebishev,y_chebishev) for i in np.array(x_plt)], 'green')


   # ax.plot(x_node, y_node, 'ro', markersize=10)


    ax.plot(x_chebishev, y_chebishev, 'ro', markersize=10)
    ax.plot(x_plt, y_plt, 'grey')
    ax.grid()
    plt.show()

#чебышевское пространство(max(|f(x)-L(x)|))
