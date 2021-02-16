# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 23:58:23 2021

@author: palom
"""

import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

# Get x values for the waves
time = np.arange(0, .0035, 0.00000001);

# DC Voltage
dcVoltage = time * 0 + 1

# Triangle Wave
triWave = 2 * signal.sawtooth(2 * np.pi * 1000 * time, 0.5)

# Sine Wave
sinWave = 0.2 * np.sin(2 * np.pi * time  * 10000)

# V-Out
vOut = dcVoltage + triWave + sinWave

# Plotting
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10
fig_size[1] = 10
plt.rcParams["figure.figsize"] = fig_size
fig, ax = plt.subplots(2,2)
# plt.rcParams['axes.grid'] = True

ax[0, 0].grid()
ax[0, 0].plot(time, dcVoltage)
ax[0, 0].set_title('DC Voltage')
ax[0, 1].grid()
ax[0, 1].plot(time, triWave, 'tab:orange')
ax[0, 1].set_title('Triangle Wave')
ax[1, 0].grid()
ax[1, 0].plot(time, -sinWave, 'tab:green')
ax[1, 0].set_title('Sine Wave')
ax[1, 1].grid()
ax[1, 1].plot(time, -vOut, 'tab:red')
ax[1, 1].set_title('V-Out')

for ax in ax.flat:
    ax.set(xlabel='Time (Seconds)', ylabel='Amplitude')

# Hide x labels and tick labels for top plots and y ticks for right plots.
#for ax in ax.flat:
#    ax.label_outer()