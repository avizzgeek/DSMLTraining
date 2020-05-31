
import numpy as np
import scipy.linalg as la


def parseInput(inputStr):
    LHS = inputStr.split("=")[0]
    RHS = inputStr.split("=")[1]
    print("LHS is", LHS)
    print("RHS is", RHS)

    #Find the co-efficients and function of lHS
    LHSCoef = LHS.split("F")
    LHSEquation = LHSCoef[1][1:4]
    if LHSCoef[0] == '':
        LHSCoef = int(1)
    else:
        LHSCoef = int(LHSCoef[0])

    print(LHSCoef)
    print(LHSEquation)

    #Find the c0-efficients and functions of RHS
    RHSEq = RHS.split(" + ")
    RHSCoef = []
    RHSPow = []
    for eq in RHSEq:
        coef = eq.split("F")[0]
        if coef == '':
            RHSCoef.append(1)
        else:
            RHSCoef.append(int(coef))

        pow = eq.split("F")[1][1:-1]
        if pow != 'K':
            RHSPow.append(int(pow.split("+")[1]))
        else:
            RHSPow.append(0)
        RHSCoef = [int(x/LHSCoef) for x in RHSCoef]


    #RHSCoef and RHS differential equation order.
    print(RHSCoef)
    print(RHSPow)

    #Construct the Array.
    #Uk+1 = AUk
    #Creating A in the differential system.
    Matrix = np.identity(len(RHSCoef))
    #Swap Row 1 with row 2.
    #swap row 2 with row 3.
    Matrix[[0,1]] = Matrix[[1,0]]
    Matrix[[1,2]] = Matrix[[2,1]]
    #put RHSCoef to row 3 on Matrix.
    Matrix[2] = RHSCoef

    #find Eigen Values of Matrix.
    eigVal,eigVec = la.eig(Matrix)
    eigVal = eigVal.real

    for x in eigVal:
        if x > 1 or x < -1:
            return False
    return True

if __name__ == "__main__":
    inputStr = "F(K+3)=2F(K+2) + 3F(K+1) + 4F(K)"
    if parseInput(inputStr):
        print("Stable")
    else:
        print("Unstable")
