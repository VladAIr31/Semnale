import numpy as np 
import matplotlib.pyplot as plt
import math

f = 6
t = np.linspace(0,1,1000)
x = np.sin(2*np.pi*f*t)


y = x*np.exp(-2j*np.pi*t)
distanta_y = np.abs(y)


fig1, axes1 = plt.subplots(1, 2, figsize=(12, 5))
axes1[0].plot(t, x, color='green')
axes1[0].axhline(0, color='black', linewidth=0.5)


scatter1 = axes1[1].scatter(y.real, y.imag, c=distanta_y, cmap='coolwarm', s=2)
axes1[1].set_xlabel("Real")
axes1[1].set_ylabel("Imaginar")
axes1[1].axhline(0, color='black', linewidth=0.5)
axes1[1].axvline(0, color='black', linewidth=0.5)



plt.tight_layout()
plt.savefig("ex2fig1.pdf")
plt.show()

omega_values = [1, 2, 3, 5, 6, 7, 11,12] 
fig2, axes2 = plt.subplots(2, 4, figsize=(10, 10))
axes2 = axes2.flatten()

for i, omega in enumerate(omega_values):
    z = x * np.exp(-2j * np.pi * omega * t)
    distanta_z = np.abs(z)
    
    axes2[i].scatter(z.real, z.imag, c=distanta_z, cmap='coolwarm', s=2)
    axes2[i].set_title(f"omega = {omega} Hz")
    axes2[i].set_xlabel("Real")
    axes2[i].set_ylabel("Imaginar")
    axes2[i].axhline(0, color='black', linewidth=0.5)
    axes2[i].axvline(0, color='black', linewidth=0.5)
    axes2[i].axis('equal')

plt.tight_layout()
plt.savefig("ex2fig2.pdf")
plt.show()