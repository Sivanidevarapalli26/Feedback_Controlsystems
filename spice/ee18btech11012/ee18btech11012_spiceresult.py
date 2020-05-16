import numpy as np  
import matplotlib.pyplot as plt


#if using termux
import subprocess
import shlex
#end if

data=np.loadtxt('ee18btech11012.dat')  
plt.plot(data[:,0],data[:,1])  
plt.grid()
plt.xlabel("time in sec")
plt.ylabel("Closed loop system magnitude response")
plt.title('Spice simulation for unity buffer system')



#if using termux
plt.savefig('./figs/ee18btech11012/ee18btech11012_spiceresult.pdf')
plt.savefig('./figs/ee18btech11012/ee18btech11012_spiceresult.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11012/ee18btech11012_spiceresult.pdf"))
#else
#plt.show()
