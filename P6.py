# -*- coding: utf-8 -*-
"""
Created on Mon May 18 21:28:31 2020

@author: Himanshu Tyagi
"""

import numpy as np
import matplotlib.pyplot as plt
n=512   ##n should be a power of 2
x_min=-5; x_max=5 ;dx=(x_max-x_min)/n
x_sample=np.arange(-5,5,dx)
sampled_data=np.full(n,5)
xfft_n=np.fft.fft(sampled_data,norm='ortho')
k_sample=np.fft.fftfreq(n,dx)
xft=np.zeros(n)
for i in range(n):
    phase=np.exp(-1j*2*np.pi*k_sample[i]*x_min)
    xft[i]=dx*np.sqrt(n/(2*np.pi))*phase*xfft_n[i]

plt.plot(x_sample,sampled_data,'-')
plt.title('f(x)',fontweight='bold',fontsize=16)
plt.xlabel('x',fontweight='bold')
plt.ylabel('f(x)',fontweight='bold')
plt.show()
plt.plot(k_sample,xft)
plt.title('Fourier Transform',fontweight='bold',fontsize=16,)
plt.xlabel('k',fontweight='bold')
plt.ylabel('ft(k)',fontweight='bold')
plt.show()