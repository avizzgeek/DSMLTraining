import sympy as sym
from sympy import Subs, Function
import numpy as np
import math
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


x = sym.Symbol('x')
y = sym.Symbol('y')

Yarray = [ ]
Xarray = [ ]
TYarray = [ ]



def find_value_of_equation(expr, xval,yval):
    substitutedValue = expr.subs(x, xval)
    substitutedValue = substitutedValue.subs(y,yval)

    return substitutedValue


def findDirDerivative(expression,xcod,ycod,zcod):
    #expression
    x, y, z = sym.symbols('x y z')
    #lhs = expression.split("=")[0]

    grad1 = sym.diff(expression, x)
    grad2 = sym.diff(expression, y)
    grad3 = sym.diff(expression, z)
    gradList = [ ]
    gradList.append(grad1.subs(x, xcod))
    gradList.append(grad2.subs(y, ycod))
    gradList.append(grad3.subs(z, zcod))

    unitVector = [ ]
    sqr = np.sqrt(xcod**2+ycod**2+zcod**2)
    unitVector.append(xcod/sqr)
    unitVector.append(ycod/sqr)
    unitVector.append(zcod/sqr)

    directionaDerivative = gradList[0]*unitVector[0] + gradList[1]*unitVector[1] + gradList[2]*unitVector[2]

    return directionaDerivative

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
    xvallist = []
    yvallist = []
    zvallist = []
    for aval in np.arange(0,5,0.5):
        min = aval - 0.5
        max = aval + 0.5
        i = 0
        for xval in np.arange(min,max,0.1):
            for yval in np.arange(min,max,0.1):
                zval = find_value_of_equation(expr, xval,yval)
                xvallist.append(int(xval))
                yvallist.append(int(yval))
                zvallist.append(int(zval))



    print("{0},{1},{2}".format(xvallist,yvallist,zvallist))
    # Data for three-dimensional scattered points


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y, z = axes3d.get_test_data(0.05)
    ax.plot_wireframe(x, y, z, rstride=5, cstride=5)
    plt.show()


if __name__ == "__main__":
    expr = x**5+y**5
    driverCode(expr)
