# -*- coding: utf-8 -*-
"""
Created on Mon May 18 21:28:31 2020

@author: Himanshu Tyagi
"""

import numpy as np
import matplotlib.pyplot as plt
data_file= np.loadtxt('noise.txt')

x=np.arange(len(data_file))
plt.plot(x,data_file)
plt.title('Noise',fontweight='bold',fontsize=16)
plt.show()

datafft=np.fft.fft(data_file)
k_data=2*np.pi*np.fft.fftshift(np.fft.fftfreq(len(data_file),1))
pdg=(np.abs(datafft)**2)/(len(datafft)*2*np.pi)

plt.plot(k_data,np.real(datafft))
plt.title('Real DFT',fontweight='bold',fontsize=16)
plt.show()
plt.plot(k_data,np.imag((datafft)))
plt.title('Imaginary DFT',fontweight='bold',fontsize=16)
plt.show()
plt.plot(k_data,pdg)
plt.title('Power Spectrum',fontweight='bold',fontsize=16)
plt.show()    
from scipy import stats
k_bin, pdg_bin, binnumber= stats.binned_statistic(k_data, pdg, bins=10)
av_pdg_bin=(pdg_bin[0:len(pdg_bin)-1]+pdg_bin[1:len(pdg_bin)])/2
plt.bar(av_pdg_bin, k_bin, width=pdg_bin[1]-pdg_bin[0])
plt.show()