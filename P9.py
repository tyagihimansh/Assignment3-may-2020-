# -*- coding: utf-8 -*-
"""
Created on Tue May 19 18:32:04 2020

@author: Himanshu Tyagi
"""

import numpy as np
import matplotlib.pyplot as plt
def f(x):
    f = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] < 1 and x[i] > -1:
            f[i] = 1
        else:
            f[i] = 0
    return f

n = 1024
x = np.linspace(-5,5,n+1)
td_f = np.fft.fft(f(x), norm='ortho')
h = td_f**2
dx=(x[1]-x[0])
convolution = np.sqrt(n)*dx*np.fft.fftshift(np.fft.ifft(h, norm='ortho'))
plt.plot(x, f(x), 'b', label="Box Function")
plt.plot(x, np.real(convolution), 'k', label="Convolution")
plt.legend()
plt.show()