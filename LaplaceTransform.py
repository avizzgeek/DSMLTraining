import numpy as np
import sympy as sy
import math
from sympy.abc import t,s
from sympy import Function, Derivative
from scipy.integrate import odeint
import re

t, s = sy.symbols('t s')
y = sy.Function('f')(t)


def laplace(expr):
    lhs = expr[0]
    rhs = expr[1]
    equation = f'{lhs}{rhs}'
    print(equation)
    lap1 = sy.laplace_transform(rhs, t, s)
    print(sy.apart(lap1))
    expr = sy.Eq(lhs, 0)
    #expr = sy.Eq(f'(t)'*10*sy.exp(-s*t),0)
    print("LSH:",expr)
    lhs_intg=sy.integrate(sy.dsolve(expr), (t, 0, sy.oo))
    print(lhs_intg)



if __name__ == "__main__":
    t,s = sy.symbols('t s')
    y = sy.Function('f')(t)
    y_ = sy.diff(y, t)
    y__ = sy.diff(y_)
    #expr = (y__ -2*y_ + 10*y, 6*sy.cos(3*t) - sy.sin(3*t))
    #passing only one term from lhs
    expr = (y__, 6 * sy.cos(3 * t) - sy.sin(3 * t))
    # print(expr)
    laplace(expr)
