import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0,0.05, step=0.00005)
f=400
s1= np.sin(2*np.pi*t*f+np.pi/3)
s2= np.sin(2*np.pi*t*f+np.pi/6)
s3= np.sin(2*np.pi*t*f+2*np.pi/3)
s4= np.sin(2*np.pi*t*f+np.pi)

z=np.random.normal(size=1000)
normaz=np.linalg.norm(z,ord=2)
normas1=np.linalg.norm(s1,ord=2)

snr=[0.1,1,10,100]


plt.plot(t, s1, color='blue')
plt.plot(t, s2, color='red')
plt.plot(t, s3, color='green')
plt.plot(t, s4, color='purple')
plt.savefig('2.1.pdf')
plt.show()

plt.close()

n=4
fig, axs = plt.subplots(n)
pl=0
for s in snr:   
    y=np.sqrt(normas1**2/(s*(normaz**2)))
    semnal=s1+y*z
    axs[pl].plot(t,semnal)
    axs[pl].set_title(s)
    pl+=1

plt.tight_layout()

plt.savefig('2.2.pdf')
plt.show()
plt.close(fig)
