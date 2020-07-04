import cmath
import math
from sympy import sympify
import numpy as np
import sympy as sym
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

s = sym.symbols('s')
f = sym.Function('f')
#original Expression dydt2 - 2*dydt + 10*y - 6*cos(3*t) + sin(3*t), calulated laplace transform manually.
expr = sym.Eq((2*s**3+4*s**2+24*s+39)/((s**2+9)*(s**2-2*s+10)), f(s))
alpha_lst = [ ]
ohmega_lst = [ ]
FS_lst = [ ]

#s=alpha+i(Ohmega)
for alpha in np.arange(-10,10,1):
    for ohmega in np.arange(-10,10,1):
        sval = complex(alpha,ohmega)
        soln = expr.lhs.subs(s,sval)
        real = sym.re(soln.n())
        img = sym.im(soln.n())
        absVal = math.sqrt(real**2 + img**2)
        FS = round(absVal,3)
        alpha_lst.append(alpha)
        ohmega_lst.append(ohmega)
        FS_lst.append(FS)

print(alpha_lst)
print(ohmega_lst)
print(FS_lst)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
m = 'o'
for xs,ys,zs in zip(alpha_lst,ohmega_lst,FS_lst):
    ax.scatter(xs, ys, zs, marker=m)

plt.show()
