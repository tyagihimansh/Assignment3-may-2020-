# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:16:00 2020

@author: Himanshu Tyagi
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as ft
import time
range = np.round(np.geomspace(2**2, 2**8, 16)).astype(int)
ffttime = []
dfttime = []
dft2time = []
for i in range:
    np.random.seed(3)
    x = np.linspace(0, 10, i)
    y = np.random.rand(i)
    t0 = time.time()
    Yfft = ft.fft(y)
    t1 = time.time()
    ffttime.append(t1 -t0)
    t01 = time.time()
    M = np.zeros([i, i], dtype=np.complex)
    m = np.arange(i)                         
    k = np.reshape(m, (i, 1))
    M = np.exp(2j * m * k * np.pi / i)
    t11 = time.time()
    ydft = np.dot(M, y)
    t12 = time.time()
    dfttime.append(t12 - t01)
    dft2time.append(t12 - t11)
    
plt.plot(range, np.array(ffttime), label='fft')
plt.plot(range, np.array(dft2time), label='dft (without M)')
plt.plot(range, np.array(dfttime), label='dft (with M)')
plt.legend()
plt.xlabel('N')
plt.ylabel('Time(sec)')
plt.title('time(dft vs fft)')
plt.show()
plt.plot(x, np.real(Yfft), label="fft")
plt.plot(x, np.real(ydft), label="dft")
plt.legend()
plt.title('Fourier tranform (using dft and fft)')
plt.show()