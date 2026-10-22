import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap


f = 400

t = np.arange(0,1,step=1/1600)

semnal = np.sin(2 * np.pi * f * t)

n=4
fig, axs = plt.subplots(n)

axs[0].plot(t,semnal)
axs[0].set_title('a')


f=800
t=np.arange(0,3,step=1/8000)
semnal = np.sin(2 * np.pi * f * t)
axs[1].plot(t,semnal)
axs[1].set_title('b')



f=240
t=np.arange(0,1,step=1/8000)
semnal= (f*t) % 1
axs[2].plot(t,semnal)
axs[2].set_title('c')

f=300 
t=np.arange(0,1,step=1/8000)
semnal= np.sign(np.sin(2*np.pi*f*t))
axs[3].plot(t,semnal)
axs[3].set_title('d')











for ax in axs.flat:
    ax.set_xlim([0,0.1])
plt.tight_layout()

plt.savefig('2abcd.pdf')
plt.show()
plt.close(fig)


a=np.random.rand(128,128)
plt.imshow(a)

plt.savefig('2e.pdf')
plt.show()
plt.close(fig)

a = np.zeros((128, 128))
a[:, 43:85] = 1
a[:, 85:] = 2

culori_romania = ListedColormap(['#002B7F', '#FCD116', '#CE1126'])
plt.imshow(a, cmap=culori_romania)

plt.savefig('2f.pdf')
plt.show()
plt.close(fig)

# 3 a)0.0005 s=1/2000
#   b) 3600000 bytes = 2000*3600*4/8


