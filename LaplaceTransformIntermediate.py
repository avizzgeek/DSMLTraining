import cmath
from sympy import sympify
x = 3
y = 4 
z = complex(x,y)
print(z)
#ab = abs(z)
#print(ab)
#expr = sym.Eq((2*s**3+4*s**2+24*s+39)/((s**2+9)*(s**2-2*s+10)), f(s))
expr = sym.Eq(2*s**3+4*s**2+24*s+39, f(s))
print(expr.lhs)
#func = sym.lambdify(s,expr.lhs,'numpy')
#print(func(1))
#alpha = round(expr.lhs.subs(s,x),3)
#print(alpha)
#Ohmega = round(float(expr.lhs.subs(s,y)),3)
#print(Ohmega)
soln = expr.lhs.subs(s,z)
print(soln)
