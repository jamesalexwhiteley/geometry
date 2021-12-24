
# general vector field visualisation https://krajit.github.io/sympy/vectorFields/vectorFields.html

import numpy as np
import matplotlib.pyplot as plt

# spacing between arrows
dx, dy = 0.8, 0.8

# control the extent of the x and y axis
xx = np.arange(-5, 5, dx)
yy = np.arange(-5, 5, dy)

x, y = np.meshgrid(xx, yy, indexing='ij')

# u = x/np.sqrt(x**2 + y**2)
# v = y/np.sqrt(x**2 + y**2)
u = 1 
v = 1

colour = 0.5
plt.quiver(x,y,u,v,colour)
# plt.show()

# u = -y/np.sqrt(x**2 + y**2)
# v = x/np.sqrt(x**2 + y**2)
u = -1 
v = -1

colour = v # colour relates to value 

plt.quiver(x,y,u,v,colour)
plt.show()

