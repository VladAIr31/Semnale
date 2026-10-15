import numpy as np
import matplotlib.pyplot as plt 


t=np.arange(0,0.03, step=0.00005)


x=np.cos(520*np.pi*t + np.pi/3)
y=np.cos(280*np.pi*t - np.pi/3)
z=np.cos(120*np.pi*t + np.pi/3)


n=3
fig, axs = plt.subplots(n)

axs[0].plot(t,x)
axs[1].plot(t,y)
axs[2].plot(t,z)


axs[0].set_title('x(t) = cos(520πt + π/3)')
axs[1].set_title('y(t) = cos(280πt − π/3)')
axs[2].set_title('z(t) = cos(120πt + π/3)')



for ax in axs.flat:
    ax.set_xlim([0,0.03])


plt.tight_layout()
plt.savefig('1a.pdf')
plt.show()
plt.close(fig)
#-------------------------------------------------------




ts=np.arange(0,0.03, step=0.00005)


x=np.cos(520*np.pi*ts + np.pi/3)
y=np.cos(280*np.pi*ts - np.pi/3)
z=np.cos(120*np.pi*ts + np.pi/3)


n=3
fig, axs = plt.subplots(n)

axs[0].stem(ts,x)
axs[1].stem(ts,y)
axs[2].stem(ts,z)


axs[0].set_title('x(t) = cos(520πt + π/3)')
axs[1].set_title('y(t) = cos(280πt − π/3)')
axs[2].set_title('z(t) = cos(120πt + π/3)')



for ax in axs.flat:
    ax.set_xlim([0,0.03])


plt.tight_layout()
plt.savefig('1b.pdf')
plt.show()