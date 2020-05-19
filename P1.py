# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:59:29 2020

@author: Himanshu Tyagi
"""

import numpy as np
def f(x):
    if (x!=0):
        return np.sin(x)/x
    else:
        return 1
x_min=-100; x_max=100
n=400
dx=(x_max-x_min)/(n-1)
sampled_data=np.zeros(n)
x_sample=np.zeros(n)
for i in range(n):
    sampled_data[i]=f(x_min+dx*i)
    x_sample[i]=x_min+i*dx
       
xfft_n=np.fft.fft(sampled_data,norm='ortho')
k_sample=np.fft.fftfreq(n,d=dx)
xft=np.zeros(n)
for i in range(n):
    phase=np.exp(-1j*2*np.pi*k_sample[i]*x_min)
    xft[i]=dx*np.sqrt(n/(2*np.pi))*phase*xfft_n[i]
import matplotlib.pyplot as plt
plt.title('f(x)',fontweight='bold',fontsize=16)
plt.plot(x_sample,sampled_data,'-')
plt.xlabel('x',fontweight='bold')
plt.ylabel('f(x)',fontweight='bold')
plt.show()
plt.plot(k_sample,xft)
plt.title('Fourier Transform',fontweight='bold',fontsize=16,)
plt.xlabel('k',fontweight='bold')
plt.ylabel('ft(k)',fontweight='bold')
plt.show()