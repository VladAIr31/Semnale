import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap
import scipy
import sounddevice

n=3
fig, axs = plt.subplots(n)

t=np.arange(0,1,step=1/44100)

f=400
semnalsinus= np.sin(2*np.pi*f*t)

semnalpatrat=np.sign(np.sin(2*np.pi*f*t))


semnalsuma=semnalsinus+semnalpatrat

axs[0].plot(t,semnalsinus)
axs[0].set_title('sinus')

axs[1].plot(t,semnalpatrat)
axs[1].set_title('patrat')


axs[2].plot(t,semnalsuma)
axs[2].set_title('suma')



for ax in axs.flat:
    ax.set_xlim([0,0.1])
plt.tight_layout()
plt.savefig('4.pdf')
plt.show()
plt.close(fig)
