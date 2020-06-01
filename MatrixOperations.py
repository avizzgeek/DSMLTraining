#Author: Avinandan Behera
#Matrix operations using numpy modules.
'''
Operations:
Matrix Multiplcations
Matrix addition
Matrix subtraction
Transpose of a matrix
Inverse matrix
find eigen values and eigen vectors
Rotate matrix
matrix diagonalization
find power of a matrix
'''

import numpy as np
import scipy.linalg as la
from random import randint


def matMultiplication(Matrix1,Matrix2):
    #before matrix multiplication lets verify if number of column in Matrix1 is equal to number of rows in Matrix2.
    Mat1RowsNo = np.size(Matrix1,0)
    Mat1ColNo = np.size(Matrix1,1)
    Mat2RowsNo = np.size(Matrix2, 0)
    Mat2ColNo = np.size(Matrix2, 1)
    if Mat1ColNo != Mat2RowsNo:
        #matrix multiplication not possible.
        print("Matrix multiplication not possible")
        return False
    result = np.dot(Matrix1,Matrix2)
    return result

def matAddition(Matrix1,Matrix2):
    # before matrix addition  lets verify if dimensions of both matrix is same.
    Mat1RowsNo = np.size(Matrix1, 0)
    Mat1ColNo = np.size(Matrix1, 1)
    Mat2RowsNo = np.size(Matrix2, 0)
    Mat2ColNo = np.size(Matrix2, 1)
    if Mat1RowsNo !=Mat2RowsNo or Mat1ColNo != Mat2ColNo:
        #Matrix addition can not be performed
        print("Matrix Addition not possible")
        return False
    result = np.add(Matrix1,Matrix2)
    return result

def matSubtraction(Matrix1, Matrix2):
    #before matrix subtraction lets verify the dimensions of both matrix is same.
    Mat1RowsNo = np.size(Matrix1, 0)
    Mat1ColNo = np.size(Matrix1, 1)
    Mat2RowsNo = np.size(Matrix2, 0)
    Mat2ColNo = np.size(Matrix2, 1)
    if Mat1RowsNo !=Mat2RowsNo or Mat1ColNo != Mat2ColNo:
        #Matrix addition can not be performed
        print("Matrix Subtraction not possible")
        return False
    result = np.subtract(Matrix1,Matrix2)
    return result

def matrixTranspose(Matrix1):
    result = np.matrix.transpose(Matrix1)
    return result

def matrixInverse(Matrix1):
    result = np.linalg.inv(Matrix1)
    return result

def getEigenValandVec(Matrix):
    result = la.eig(Matrix)
    return result

def diagonalizeMatrix(Matrix):
    eig = getEigenValandVec(Matrix)
    eigVal = eig[0]
    eigVec = eig[1]
    eigVal = eigVal.real

    d = np.diag(eigVal)
    eigVecInv = matrixInverse(eigVec)
    return eigVec, d, eigVecInv

def matrixPower(Matrix,power):
    eigVec, eigVal, eigVecInv = diagonalizeMatrix(Matrix)
    eigVal = eigVal.real
    eigValPow = np.power(eigVal,power)
    result = eigVec @ eigValPow @ eigVecInv

    return result

if __name__ == "__main__":
    #get the size of array
    row, column = input("Enter the no of row and column in Matrix with space seperated").split()
    print("Rows:",row)
    print("Columns:",column)
    row = int(row)
    column = int(column)
    #create a list of random numbers and reshape that to matrix with user given dimensions.
    Matrix_1 = []
    for _ in range(row*column):
        Matrix_1.append(randint(0, row*column))

    #print(matrix_elem)
    #reshape the matrix as per user given dimension.
    Matrix_1 = np.reshape(Matrix_1,(row, column))
    print(Matrix_1)

    #prepare second matrix
    Matrix_2 = []
    for _ in range(row * column):
        Matrix_2.append(randint(0, row * column))

    # print(matrix_elem)
    # reshape the matrix as per user given dimension.
    Matrix_2 = np.reshape(Matrix_2, (row, column))
    print(Matrix_2)

    #Multiply Matrix1 and Matrix2
    print("Matrix Multiplication of Matrix1 * Matrix2")
    print(matMultiplication(Matrix_1,Matrix_2))
    print("Matrix Additon of Matrix1 + Matrix2")
    print(matAddition(Matrix_1,Matrix_2))
    print("Matrix Subtraction of Matrix1 + Matrix2")
    print(matSubtraction(Matrix_1, Matrix_2))
    print("Matrix Transpose of Matrix1")
    print(matrixTranspose(Matrix_1))
    print("Matrix Inverse of Matrix1")
    print(matrixInverse(Matrix_1))
    print("Eigen Values of Matrix1")
    eigList = getEigenValandVec(Matrix_1)
    eigVal = eigList[0]
    eigVal = eigVal.real
    print(eigVal)
    print("Eigen Vectors of Matrix1")
    print(eigList[1])
    print("Diagonalize the Matrix1")
    print(diagonalizeMatrix(Matrix_1))
    print("Find power of matrix")
    power = input("Enter the power of Matrix")
    power = int(power)
    print("Power %d of Matrix is" %power)
    print(matrixPower(Matrix_1,power))
