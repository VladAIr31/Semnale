import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(-np.pi/2, np.pi/2, 1000)

sin_a = np.sin(a)
aprox_taylor = a
aprox_pade = (a - (7 * a**3) / 60) / (1 + (a**2) / 20)

eroare_taylor = np.abs(sin_a - aprox_taylor)
eroare_pade = np.abs(sin_a - aprox_pade)

n = 3
fig, axs = plt.subplots(n, figsize=(8, 10))

axs[0].plot(a, sin_a, label='sin(a)')
axs[0].plot(a, aprox_taylor, label='Aproximare Taylor (a)')
axs[0].plot(a, aprox_pade, label='Aproximare Pade')
axs[0].legend()
axs[0].set_title('Comparare funcții')

axs[1].plot(a, eroare_taylor, label='Eroare Taylor')
axs[1].plot(a, eroare_pade, label='Eroare Pade')
axs[1].legend()
axs[1].set_title('Eroarea de aproximare')


axs[2].plot(a, eroare_taylor, label='Eroare Taylor')
axs[2].plot(a, eroare_pade, label='Eroare Pade')
axs[2].set_yscale('log')
axs[2].legend()
axs[2].set_title('Eroarea de aproximare (axa Oy logaritmică)')

for ax in axs.flat:
    ax.set_xlim([-np.pi/2, np.pi/2])

plt.tight_layout()
plt.savefig('8.pdf')
plt.show()
plt.close(fig)