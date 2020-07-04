from sympy import Function, dsolve, Eq, Derivative, sin, cos, symbols
from sympy.abc import x
import sympy as sym
import matplotlib.pyplot as plt
import numpy as np


sym.init_printing()
t = symbols('t')
y = Function('y')(t)
dydt = y.diff(t)
dydt2 = dydt.diff(t)
expr = Eq(dydt2 - 2*dydt + 10*y - 6*cos(3*t) + sin(3*t), 0)
print(expr)
t = sym.symbols('t')
f = Function('y')
soln = dsolve(expr, f(t))
print(soln)
constants = sym.solve([soln.rhs.subs(t,0) - 2, soln.rhs.diff(t,1).subs(t,0) + 8])
C1, C2 = sym.symbols('C1,C2')
soln = soln.subs(constants)
func = sym.lambdify(t,soln.rhs,'numpy')

timeList = [ ]
FOut = [ ]
for k in np.arange(-10,10,1):
    v = func(k)
    timeList.append(k)
    FOut.append(round(v,2))


plt.plot(timeList,FOut,'red')
plt.show()
