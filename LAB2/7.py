import numpy as np
import matplotlib.pyplot as plt


tinit=np.arange(0,1, step=1/1000)

semnal=np.sin(2*np.pi*tinit*100)
t1=tinit[::4]       
semnal1=semnal[::4]

t2=tinit[1::4]      
semnal2=semnal[1::4]

n=3
fig, axs = plt.subplots(n)
axs[0].plot(tinit,semnal)

axs[1].plot(t1,semnal1)


axs[2].plot(t2,semnal2)


for ax in axs.flat:
    ax.set_xlim([0,0.5])
plt.tight_layout()
plt.savefig('7.pdf')
plt.show()
plt.close(fig)