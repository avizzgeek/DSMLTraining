import numpy as np
import sympy as sy
from math import *
from random import randint,uniform


def grad_diff(expression):
    expression = expression.split("=")
    print(expression)
    rhs = expression[1]
    #create symbols
    x, y = sy.symbols('x y')

    grad1 = sy.diff(rhs, x)
    grad2 = sy.diff(rhs, y)

    flag = True
    gradValList = []
    i = randint(1, 10)
    j = randint(1, 10)
    newgradval1 = grad1.subs(x, i)
    newgradval2 = grad2.subs(y, j)
    gradValList.append(newgradval1)
    gradValList.append(newgradval2)
    unitVector = []
    icap = i / sqrt(i ** 2 + j ** 2)
    jcap = j / sqrt(i ** 2 + j ** 2)
    unitVector.append(icap)
    unitVector.append(jcap)
    initialDirDerivative = newgradval1*icap + newgradval2 * jcap

    while (flag):
        #Find Directional derivative.
        i = randint(1, 10)
        j = randint(1, 10)
        newgradval1 = grad1.subs(x, i)
        newgradval2 = grad2.subs(y, j)
        print("Grad value 1:{0} 2:{1}".format(newgradval1,newgradval2))
        nextDirDerivative = 0
        sqr = np.sqrt(i**2 + j**2)
        print("SQUAREROOT:",sqr)
        icap = i/sqr
        jcap = j/sqr
        unitVector.append(icap)
        unitVector.append(jcap)
        nextDirDerivative = newgradval1*icap + newgradval2 * jcap
        #now multiply U vector with grad vector.
        print("i:{0} j:{1}".format(i,j))
        print("icap:{0} jcap{1}".format(icap,jcap))
        print("i:{0} j:{1}".format(i, j))
        if (nextDirDerivative - initialDirDerivative) > 0:
            if(newgradval1 == 0 or newgradval2 ==0):
                #stop the loop we found the saddle point.
                print("Saddle point is found at ({0},{1})".format(i,j))
                break
            initialDirDerivative = nextDirDerivative
        else:
            continue


if __name__ == "__main__":
    expression = "x**2/4-y**2/6=z/8"
    grad_diff(expression)


