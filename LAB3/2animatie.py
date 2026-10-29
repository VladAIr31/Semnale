import numpy as np 
import matplotlib.pyplot as plt

f = 6
t = np.linspace(0,1,1000)
x = np.sin(2*np.pi*f*t)


y = x * np.exp(-2j*np.pi*t)
distanta_y = np.abs(y)

plt.ion() 

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

viteza = 10 
for i in range(0, len(t), viteza):
    ax1.clear() 
    ax2.clear()
    

    ax1.set_xlim(0, 1)
    ax1.set_ylim(-1.2, 1.2)
    ax1.set_title("Semnalul în timp")
    ax1.set_xlabel("Timp (s)")
    ax1.set_ylabel("Amplitudine")
    ax1.axhline(0, color='black', linewidth=0.5)
    
    ax1.plot(t, x, color='green', alpha=0.5)
    ax1.plot(t[i], x[i], 'ro', markersize=8)
    ax1.plot([t[i], t[i]], [0, x[i]], 'r-')

 
    ax2.set_xlim(-1.1, 1.1)
    ax2.set_ylim(-1.1, 1.1)

    ax2.set_xlabel("Real")
    ax2.set_ylabel("Imaginar")
    ax2.axhline(0, color='black', linewidth=0.5)
    ax2.axvline(0, color='black', linewidth=0.5)
    ax2.set_aspect('equal') 
    
    ax2.scatter(y.real[:i], y.imag[:i], c=distanta_y[:i], cmap='coolwarm', s=2)
    
    ax2.plot(y.real[i], y.imag[i], 'ro', markersize=8)
    
    ax2.plot([0, y.real[i]], [0, y.imag[i]], 'r-', alpha=0.5)
    
    plt.pause(0.01) 

plt.ioff()
plt.show()