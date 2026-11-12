import numpy as np 
import matplotlib.pyplot as plt


fs = 300
T = 0.05 


t_continuu = np.linspace(0, T, 1000) 
t_discret = np.arange(0, T, 1/fs)

f1,f2,f3 = 200, 100, 500 

s1_continuu = np.cos(2 * np.pi * f1 * t_continuu)
s2_continuu = np.cos(2 * np.pi * f2 * t_continuu)
s3_continuu = np.cos(2 * np.pi * f3 * t_continuu)

esantioane = np.cos(2 * np.pi * f1 * t_discret)

fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

axs[0].plot(t_continuu, s1_continuu, color='#aaaaff', linewidth=2, label='200 Hz')
axs[0].plot(t_discret, esantioane, 'yo', markersize=8, label='Eșantioane (fs=300 Hz)')

axs[1].plot(t_continuu, s2_continuu, color='#aa0055', linewidth=2, label='100 Hz')
axs[1].plot(t_discret, esantioane, 'yo', markersize=8)

axs[2].plot(t_continuu, s3_continuu, color='#005522', linewidth=2, label='500 Hz')
axs[2].plot(t_discret, esantioane, 'yo', markersize=8)


for ax in axs:
    ax.legend(loc='upper right')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_ylim(-1.2, 1.2)
    ax.set_ylabel('Amplitudine')

axs[2].set_xlabel('Timp (secunde)')
fig.suptitle('Fenomenul de aliere: 3 semnale diferite eșantionate la fel', fontsize=14)

plt.tight_layout()
plt.show()
plt.savefig("2.pdf")

