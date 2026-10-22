import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0,1, step=0.0005)
sin = 2*np.sin(2*np.pi*t+np.pi/2)
cos = 2*np.cos(2*np.pi*t)



n=2
fig, axs = plt.subplots(n)
axs[0].plot(t,sin)
axs[1].plot(t,cos)
axs[0].set_title('sin')
axs[1].set_title('cos')
plt.tight_layout()
plt.savefig('1.pdf')
plt.show()