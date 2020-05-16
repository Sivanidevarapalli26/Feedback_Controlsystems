import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if


num = [1e5*2*np.pi*10]		#describing closed loop transfer function
den = [1,(1e5+1)*2*np.pi*10]
closedlooptf = signal.lti(num,den)

T, yout = signal.step(closedlooptf)	
plt.plot(T,yout)
plt.grid()
plt.xlabel("time (t)")
plt.title("Closed loop system response ")
plt.show()
