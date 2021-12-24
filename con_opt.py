
# CONSTRAINED OPTIMISATION PROBLEM 
# think of an elipse x^2 + 4y^2 = 4 
# with a rectangle inscribed inside, whose perimeter P = 4x + 4y 

# analytic answer 
# max  P(x,y) = 4x + 4y 
# s.t. g(x,y) = x^2 + 4y^2 = 4 
#      Px = λgx
#      Py = λgy

# LAGRANGE MULTIPLIER ∇P = λ∇g 
# it follows Px = λgx and Py = λgy

# 4 = 2λx
# 4 = 8λy
# y = 1/sqrt(5) (assumed +ve from start)
# x = 4/sqrt(5)

# critical point: (4/sqrt(5), 1/sqrt(5))
# must also check boundary 
# calc P(x,y) for these three points 


# or can plot vector fields of P and g directly 
# CENTRAL IDEA: at the maximum (highest) point, the gradient of P(x,y) will be normal to the boundary g. 
# the gradient of boundary (level) curve g(x,y) is normal to g at every point on g 
# this leads to idea of LAGRANGE MULTIPLIER ∇P = λ∇g 
import numpy as np
import matplotlib.pyplot as plt

# spacing between arrows
dx, dy = .15, .15

# control the extent of the x and y axis
x = np.arange(0, 2.5, dx)
y = np.arange(0, 2.5, dy)

xx, yy = np.meshgrid(x, y, indexing='ij')

# function P(x,y) = 4x + 4y
P = 4 * xx + 4 * yy 
# function g(x,y) = x^2 + 4y^2 
g = xx*xx + 4 * yy*yy

color = g

# calc gradient and plot gradient field 
Px, Py = np.gradient(P, dx, dy)
gx, gy = np.gradient(g, dx, dy)

plt.figure(figsize=(12,12)) 
plt.quiver(xx, yy, Px, Py, color)
plt.quiver(xx, yy, gx, gy) 

# plot constraint boundary 
dx, dy = 0.01, 0.01
x = np.arange(0, 2.5, dx)
y = np.arange(0, 2.5, dy)
xx, yy = np.meshgrid(x, y, indexing='ij')
c = 4
F = (xx)**2 + 4*(yy)**2 - c ## ellipse - cartesian equation 
plt.contour(xx,yy,F,[0])


plt.show()

