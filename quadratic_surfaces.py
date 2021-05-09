from __future__ import division
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from math import pi
from numpy import sqrt, linspace 

def setfig(dimx, dimy):
	plt.xlim(-dimx, dimy)
	plt.ylim(-dimx, dimy)
	plt.gca().set_aspect('equal', adjustable='box')
	x = np.linspace(-dimx, dimx, 100)
	y = np.linspace(-dimy, dimy, 100)
	X, Y = np.meshgrid(x,y)
	return X,Y

def setfigsurface(dimx, dimy):
	fig = plt.figure(figsize=plt.figaspect(1))  # Square figure
	ax = fig.add_subplot(111, projection='3d')
	x = np.linspace(-dimx, dimx, 100)
	y = np.linspace(-dimy, dimy, 100)
	X, Y = np.meshgrid(x,y)
	return X,Y,ax

# # PLOT ELLIPSE 
# X,Y = setfig(5, 5)
# a = 4
# b = 3
# c = 1
# F = (X/a)**2 + (Y/b)**2 - c ## ellipse - cartesian equation 
# plt.contour(X,Y,F,[0])
# plt.show()

# # PLOT PARABOLA
# X,Y = setfig(20, 20)
# a = 1/10
# b = 0
# c = -10
# F = Y - a*X**2-b*X-c  
# plt.contour(X,Y,F,[0])
# plt.show()

# # PLOT HYPERBOLA
# X,Y = setfig(20, 20)
# a = 1
# b = 1
# c = 1
# F = Y - sqrt((X/a)**2 -b**2*c)  
# plt.contour(X,Y,F,[0])
# plt.contour(X,-Y,F,[0])
# plt.show()

# # PLOT HYPERBOLOID (PARAMETRIC)
# X,Y,ax = setfigsurface(2,2*pi)
# a = 1
# b = 1
# c = 1
# x = a*np.cosh(X)*np.cos(Y)  
# y = b*np.cosh(X)*np.sin(Y)
# z = c*np.sinh(X)
# ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')
# plt.show()

# # PLOT HYPERBOLIC PARABALOID
# X,Y,ax = setfigsurface(5,5)
# a = 1
# b = 1
# Z = (X/a)** 2 - (Y/b) ** 2
# ax.plot_surface(X, Y, Z,  rstride=4, cstride=4, color='b')
# plt.show()

# # PLOT ELLIPTIC PARABALOID
# X,Y,ax = setfigsurface(5,5)
# a = 1
# b = 1
# Z = (X/a)** 2 + (Y/b) ** 2
# ax.plot_surface(X, Y, Z,  rstride=4, cstride=4, color='b')
# plt.show()