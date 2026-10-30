import numpy as np
import matplotlib.pyplot as plt


fs = 400
t = np.arange(0, 1, 1/fs) 
f1, f2, f3, f4  = 2, 27, 99, 50

x = 3*np.sin(2*np.pi*f1*t)+0.5*np.sin(2*np.pi*f2*t)+5*np.cos(2*np.pi*f3*t)+np.sin(2*np.pi*f4*t)

frecvente = np.arange(1, 101) 
modul_X = np.zeros(len(frecvente))


for i, omega in enumerate(frecvente):

    componenta = x*np.exp(-2j*np.pi*omega*t)
    X_omega = np.sum(componenta)
    modul_X[i] = np.abs(X_omega)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(t, x, color='green', linewidth=1)
ax1.set_title("Semnalul compus x(t)")
ax1.set_xlabel("Timp (s)")
ax1.set_ylabel("x(t)")
ax1.grid(True)

markerline, stemlines, baseline = ax2.stem(frecvente, modul_X, basefmt=" ")
plt.setp(markerline, markerfacecolor='none', markeredgecolor='black')
plt.setp(stemlines, color='black', linewidth=1)

ax2.set_title("Modulul Transformatei Fourier")
ax2.set_xlabel("Frecvența (Hz)")
ax2.set_ylabel("Modulul")
ax2.grid(True)

plt.tight_layout()

plt.savefig("3.pdf")
plt.show()