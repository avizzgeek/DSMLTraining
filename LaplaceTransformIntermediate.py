sym.init_printing()
t = symbols('t')
y = Function('y')(t)
dydt = y.diff(t)
dydt2 = dydt.diff(t)
expr = Eq(dydt2 - 2*dydt + 10*y - 6*cos(3*t) + sin(3*t), 0)
print(expr)

# In[25]:
t = sym.symbols('t')
f = Function('y')
# In[26]:
soln = dsolve(expr, f(t))
print(soln)
constants = sym.solve([soln.rhs.subs(t,0) - 2, soln.rhs.diff(t,1).subs(t,0) + 8])
#constants
# In[29]:
C1, C2 = sym.symbols('C1,C2')
soln = soln.subs(constants)
print(soln)
# In[30]:
func = sym.lambdify(t,soln.rhs,'numpy')
#print(func)
# In[31]:
v = func(1)
print(v)



=================

import cmath
x = 4
y = 5 
z = complex(x,y)
x = abs(z)
#print(z)
expr = sym.Eq((2*s**3+4*s**2+24*s+39)/((s**2+9)*(s**2-2*s+10)), f(s))
print(expr.lhs)
#func = sym.lambdify(s,expr.lhs,'numpy')
#print(func(1))
alpha = round(expr.lhs.subs(s,x),3)
print(alpha)
Ohmega = round(float(expr.lhs.subs(s,y)),3)
print(Ohmega)
