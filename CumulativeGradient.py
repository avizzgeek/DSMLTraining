import numpy as np
import sympy as sy
import math
from random import randint,uniform


def grad_diff(expression):
    expression = expression.split("=")
    print(expression)

    x, y = sy.symbols('x y')

    lhs=expression[0]
    rhs = expression[1]
    grad1 = sy.diff(lhs, x)
    grad2 = sy.diff(lhs, y)
    print(grad1, grad2)
    flag = True
    grad1Val = grad1.subs(x, 0)
    grad2Val = grad2.subs(y, 0)
    gradValList = []
    i = randint(0, 10)
    j = randint(0, 10)
    newgradval1 = grad1.subs(x, i)
    newgradval2 = grad2.subs(y, j)
    positivegradValList = []
    negativegradValList =[]
    while(flag):

        if newgradval1 !=0:
            i = randint(0, 10)
            newgradval1 = grad1.subs(x, i)
        if newgradval2 !=0:
            j = randint(0, 10)
            newgradval2 = grad2.subs(y,j)

        if (newgradval1 - grad1Val) > 0 or (newgradval2 - grad2Val) > 0:
            #moving towards minima
            positivegradValList = [newgradval1,newgradval2]
            grad1Val = newgradval1
            grad2Val = newgradval2
        elif (newgradval1 - grad1Val) < 0 or (newgradval2 - grad2Val) < 0:
            #moving towars maxima.
            negativegradValList = [newgradval1,newgradval2]
            #if we are here then we are moving away from saddle point., so lets stop loop here.
            flag = False

    print(positivegradValList)
    print(negativegradValList)


    #now we have two points with +ve and -ve transition.
    #we need to find the saddle point which lies in between the positivegradlist and negativegradlist points.
    #i range 7/2 --> 2
    #j range -2-->-7/3.
    iStartCond = int(positivegradValList[0])
    iStopCond = int(negativegradValList[0])
    jStartCond = int(positivegradValList[0])
    jStopCond = int(negativegradValList[0])
    while(True):
        i = uniform(iStartCond, iStopCond)
        j = uniform(jStartCond, jStopCond)
        #print("{0},{1}".format(newgradval1,newgradval2))
        newgradval1 = grad1.subs(x, i)
        newgradval2 = grad2.subs(y, j)

        newgradval1 = int(newgradval1)
        newgradval2 = int(newgradval2)
        print("{0},{1}".format(newgradval1,newgradval2))
        if newgradval1 == 0 and newgradval2 == 0:
            #we found the saddle point.
            print("Saddle point of {0} is at ({1},{2})".format(expression,i,j))
            break

if __name__ == "__main__":
    expression = "x**2/4-y**2/6=z/8"
    grad_diff(expression)


