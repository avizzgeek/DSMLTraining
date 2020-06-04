import numpy as np
import sympy as sy
from math import *
from random import randint,uniform



def validateCoordinates(x,y,z):
    result = (x**2)/4 - (y**2)/6 - z/8
    if result == 0:
        #print("Found the co-ordinates lying in the curve")
        return True


def findDirDerivative(expression,xcod,ycod,zcod):
    #expression
    x, y, z = sy.symbols('x y z')
    lhs = expression.split("=")[0]

    grad1 = sy.diff(lhs, x)
    grad2 = sy.diff(lhs, y)
    grad3 = sy.diff(lhs, z)
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


def grad_diff(expression):
    print(expression)
    #create symbols
    #find initial co-ordinate which satisfy the equation.a
    while (True):
        xcod = randint(-100, 100)
        ycod = randint(-100, 100)
        zcod = randint(-100, 100)
        if validateCoordinates(xcod,ycod,zcod):
            initDirDerivative = findDirDerivative(expression, xcod, ycod, zcod)
            initDirDerivative = round(initDirDerivative,3)
            if initDirDerivative < 0:
                #we found the initial co-ordinates to start.
                break
    print("Found Initial points to start ({0},{1},{2})".format(xcod,ycod,zcod))
    print("Initial directional derivative is ",initDirDerivative)
    #Find gradient of the given point and directional derivative in 4 different direction.
    alldirGradient = [ ]
    for val in range(xcod,xcod+100):
        if validateCoordinates(val,ycod,zcod):
            alldirGradient.append(findDirDerivative(expression,val,ycod,zcod))
    for val in range(xcod-100,xcod):
        if validateCoordinates(val,ycod,zcod):
            alldirGradient.append(findDirDerivative(expression,val,ycod,zcod))
    for val in range(ycod,ycod+100):
        if validateCoordinates(xcod,val,zcod):
            alldirGradient.append(findDirDerivative(expression,xcod,val,zcod))
    for val in range(ycod-100,ycod):
        if validateCoordinates(xcod,val,zcod):
            alldirGradient.append(findDirDerivative(expression,xcod,val,zcod))
    for val in range(zcod,zcod+100):
        if validateCoordinates(xcod,ycod,val):
            alldirGradient.append(findDirDerivative(expression,xcod,ycod,val))
    for val in range(zcod-100,zcod):
        if validateCoordinates(xcod,ycod,val):
            alldirGradient.append(findDirDerivative(expression,xcod,ycod,val))

    print(alldirGradient)





    # decide if the directional derivative sign indicates the movement towards maxima or minima.
    #if sign is -ve --> dir towards minima from maxima
    #if sign is +ve --> dir toward maxima from minima
    # we need -ve sign in directional derivative to proceed with the application.


if __name__ == "__main__":
    expression = "x**2/4-y**2/6-z/8=0"
    grad_diff(expression)



