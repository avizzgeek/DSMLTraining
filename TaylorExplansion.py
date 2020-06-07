import sympy as sym
from sympy import Subs, Function
import numpy as np
import math
import matplotlib.pyplot as plt

x = sym.Symbol('x')

Yarray = [ ]
Xarray = [ ]

TYarray = [ ]
TXarray = [ ]
def plot_graph(Yarray,Xarray,linecolor):
    plt.plot(Xarray,Yarray,color=linecolor)
    plt.ylabel('Nth order Derivative')
    plt.xlabel('X Value')
    plt.show()


def find_value_of_equation(expr, value):
    substitutedValue = expr.subs(x, value)
    return substitutedValue


def find_taylor_Expansion(expr,xvalue,avalue):
    f0 = expr.subs(x, xvalue)
    print(f0)
    sum = f0
    for i in range(1,3):
        equation = sym.diff(expr, x)
        newterm = (equation.subs(x, xvalue)) / math.factorial(i)
        xadiff = (xvalue-avalue)**i
        newterm = newterm * xadiff
        sum += newterm
    return sum


def driverCode(expr):
    #substitue different values of x
    '''for i in np.arange(-1,6,0.5):
        Yarray.append(find_value_of_equation(expr,i))
        Xarray.append(i)
        if (i >= -1 and i < 1):
            TYarray.append(find_taylor_Expansion(expr, i, 0))
        elif (i >= 1 and i < 2):
            TYarray.append(find_taylor_Expansion(expr, i, 1))
        elif (i >= 2 and i < 3):
            TYarray.append(find_taylor_Expansion(expr, i, 2))
        elif (i >= 3 and i < 4):
            TYarray.append(find_taylor_Expansion(expr, i, 3))
        elif (i >= 4 and i < 5):
            TYarray.append(find_taylor_Expansion(expr, i, 4))
        elif (i >= 5 and i < 6):
            TYarray.append(find_taylor_Expansion(expr, i, 5))'''
    for aval in np.arange(0,5,0.5):
        min = aval - 0.5
        max = aval + 0.5
        i = 0
        for xval in np.arange(min,max,0.1):
            Yarray.append(find_value_of_equation(expr, xval))
            Xarray.append(xval)
            TYarray.append(find_taylor_Expansion(expr, xval, aval))

    print("{0},{1}".format(len(TYarray),len(Xarray)))
    plt.plot(Xarray,Yarray,'red')
    plt.plot(Xarray,TYarray,'blue')
    plt.ylabel('Nth order Derivative')
    plt.xlabel('X Value')
    plt.show()

if __name__ == "__main__":
    expr = 3 * x ** 3 + x ** 2 - 8 * x + 6
    driverCode(expr)
