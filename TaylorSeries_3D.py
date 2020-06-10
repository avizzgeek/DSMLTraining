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


def getHassianMatrix(expr,xval,yval):
    #since hessain matrix is found with doube partial derivative of the equation.
    grad1 = sym.diff(expr, x)
    grad2 = sym.diff(expr, y)
    print("First Order partial derivative:F'x={0} F'y={1}".format(grad1,grad2))
    grad2x = sym.diff(grad1,x)
    grad2y = sym.diff(grad2,y)
    grad2xy = sym.diff(grad1,y)
    print("Second Order partial derivative:F''x={0} F''y={1} F''xy=F''yx={2}".format(grad2x,grad2y,grad2xy))
    HassianList = [ ]
    HassianList.append(grad2x.subs(x,xval).subs(y,yval))
    HassianList.append(grad2xy.subs(y, yval).subs(x,xval))
    HassianList.append(grad2xy.subs(y, yval).subs(x, xval))
    HassianList.append(grad2y.subs(y,yval).subs(x,xval))

    #conver the list to Hassian matrix and return the matrix.
    HassianMatrix = np.reshape(HassianList, (2, 2))
    return HassianMatrix


def getGradient(expr, xval, yval):
    gradVector = []
    x, y = sym.symbols('x y')
    grad1 = sym.diff(expr, x)
    grad2 = sym.diff(expr, y)
    gradVector.append(grad1.subs(x, xval).subs(y,yval))
    gradVector.append(grad2.subs(y, yval).subs(x,xval))
    return gradVector

def find_value_of_equation(expr, xval,yval):
    substitutedValue = expr.subs(x, xval).subs(y,yval)
    #substitutedValue = substitutedValue.subs(y,yval)

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

def find_taylor_Expansion(expr,vVector,xvalue,yvalue):
    #first term of solution F(a)
    f0 = []
    f0.append(expr.subs(x, xvalue).subs(y,yvalue))
    print(f0)
    sum = f0

    #second term of solution
    gradient = getGradient(expr,xvalue,yvalue)
    term2 = np.dot(vVector, gradient)
    sum  = np.add(sum,term2)

    #third term of the solution.
    HassianMatrix = getHassianMatrix(expr,xvalue,yvalue)
    vVector = np.reshape(vVector,(2,1))
    vVectorT = np.matrix.transpose(vVector)
    term3 = np.dot(vVectorT, HassianMatrix)
    term3 = np.dot(term3,vVector)
    term3 = 1/2*term3
    sum = np.add(sum,term3)
    return sum

def driverCode(expr):
    #substitue different values of x
    xvallist = []
    yvallist = []
    zvallist = []
    for aval2 in np.arange(0,5,0.5):
        for aval1 in np.arange(0,5,0.5):
            min = aval1 - 0.5
            max = aval1 + 0.5
            #i = 0
            for xval in np.arange(min,max,0.1):
                yval = aval2
                vVector = [ ]
                vVector.append(xval-aval1)
                vVector.append(yval-aval2)
                zval = find_taylor_Expansion(expr,vVector,xval,yval)
                xvallist.append(xval)
                yvallist.append(yval)
                zvallist.append(zval)



    print("{0}".format(zvallist))
    # Data for three-dimensional scattered points
    #plot 3-D graph
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y, z = axes3d.get_test_data(0.05)
    ax.plot_wireframe(x, y, z, rstride=5, cstride=5)
    plt.show()
    


if __name__ == "__main__":
    expr = 5*x**2+x*y**3-y**2
    driverCode(expr)
