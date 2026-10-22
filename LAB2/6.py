import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap
import scipy
import sounddevice
n=3
fig, axs = plt.subplots(n)


t=np.arange(0,1,step=1/8000)
f1=8000/2
f2=8000/4
f3=0

semnal1= np.sin(2*np.pi*f1*t)
semnal2= np.sin(2*np.pi*f2*t)
semnal3= np.sin(2*np.pi*f3*t)


axs[0].plot(t,semnal1)
axs[0].set_title('f = fs/2')

axs[1].plot(t,semnal2)
axs[1].set_title('f = fs/4')


axs[2].plot(t,semnal3)
axs[2].set_title(' f = 0 Hz')



for ax in axs.flat:
    ax.set_xlim([0,0.05])
plt.tight_layout()
plt.savefig('6.pdf')
plt.show()
plt.close(fig)