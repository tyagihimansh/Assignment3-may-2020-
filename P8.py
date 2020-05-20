# -*- coding: utf-8 -*-
"""
Created on Tue May 19 19:44:38 2020

@author: Himanshu Tyagi
"""


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
def f(x,y):
	return np.exp(-(x**2+y**2))

n=100
x=np.linspace(-50,50,n) ; y=x

X,Y = np.meshgrid(x,y)
kx = 2*np.pi*np.fft.fftshift(np.fft.fftfreq(len(x), x[1]-x[0]))
ky=kx
kX, kY= np.meshgrid(kx, ky)
f_sample=np.fft.fftshift(f(X,Y))

nft=np.fft.fftshift(np.fft.fft2(f_sample))

fig = plt.figure()
ax = fig.gca(projection='3d')
surf= ax.plot_surface(kX , kY , np.real(nft)*(x[1] - x[0])*(y[1] - y[0])/(2*np.pi) , cmap=cm.coolwarm, linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.title('using FFT2')
plt.show()
ft_analytic= 0.5*np.exp(-(kX**2+kY**2)/4)
fig1 = plt.figure()
ax1 = fig1.gca(projection='3d')
surf1= ax1.plot_surface(kX , kY , ft_analytic , cmap=cm.coolwarm, linewidth=0, antialiased=False)
fig1.colorbar(surf1, shrink=0.5, aspect=5)
plt.title('Analytic FT')
plt.show()
