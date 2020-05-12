#Code by D.Sivani
#May 12th,2020
#Released under GNU GPL


import numpy as np
import math
from scipy import signal
import control
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

#H = 1 #unity gain buffer system has feedback factor H=1
num = [1e5*20*np.pi]
den = [1,20*np.pi+1e5]
G = signal.lti(num,den)
w, mag, phase = signal.bode(G,w=np.linspace(1,1e8,100000))
sys = control.tf(num, den)
gm, pm, wpc, wgc = control.margin(sys)

print('Phase Margin in degrees:', pm)
print('Gain cross-over frequency in rad/sec:', wgc)

#Magnitude plot
plt.subplot(2, 1, 1) 
plt.semilogx(w, mag,'g') 
plt.plot(wgc, 0, 'o')
plt.text(6.283*1e6,0, '({}, {})'.format(6.283*1e6,0))
plt.ylabel("20$log_{10}(|G(j\omega)|$")
plt.title("Magnitude Plot")
plt.grid()

# Phase plot
plt.subplot(2, 1, 2) 
plt.semilogx(w, phase,'r')  
plt.plot(wgc, pm-180, 'o')
plt.text(6.283*1e6,-90, '({}, {})'.format(6.283*1e6,-90))
plt.xlabel("$\omega$ in rad/s")
plt.ylabel("$\phi(j\omega)$")
plt.title("Phase Plot")
plt.grid()


#if using termux
plt.savefig('./figs/ee18btech11012/ee18btech11012_1.pdf')
plt.savefig('./figs/ee18btech11012/ee18btech11012_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11012/ee18btech11012_1.pdf"))
#else
#plt.show()
