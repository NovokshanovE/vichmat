import random
import matplotlib.pyplot as plt
import numpy as np

def l_i(i, x, x_nodes):
    x_nodes_i = np.r_[x_nodes[:i],x_nodes[i+1:]]
    return np.prod((x-x_nodes_i)/(x_nodes[i]-x_nodes_i))
def L(x, x_nodes, y_nodes):
    return np.sum(y_nodes*[l_i(i,x,x_nodes) for i in range(x_nodes.size)])
def res(x_u,x_ch, f, k, flag):
    y_u = f(x_u)
    y_ch = f(x_ch)
    fig, ax = plt.subplots(1, 1, figsize = (6, 5))
    x_plt = np.linspace(-1,1,200)
    ax.plot(x_u, f(x_u), 'ro', markersize = 5)
    ax.plot(x_plt, f(x_plt), 'yellow')
    ax.plot(x_plt, [L(i,x_u,y_u) for i in x_plt])
    ax.plot(x_plt, [L(i, x_ch, y_ch) for i in x_plt], color = 'red')
    ax.plot(x_ch, f(x_ch), 'o', color = 'red', markersize=5)
    ax.grid()
    plt.show()
def uniform_chebishev():
    f = lambda x: 1. / (1. + 25 * x ** 2)
    for n in range(5, 24, 3):
        x_u = np.linspace(-1,1,n)
        x_ch = np.array([np.cos((2*i-1)/(2*n)*np.pi) for i in range(1, n+1)])
        res(x_u, x_ch,f, n, 'uc')
uniform_chebishev()