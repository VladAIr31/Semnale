import numpy as np 
import matplotlib.pyplot as plt
import math
import time 


def dft(x):

    N=len(x)
    n=np.arange(N)
    k=n.reshape(N,1)
    F=np.exp(-2j*np.pi*n*k/N)

    return np.dot(F,x)


def fft(x):

    N=len(x)
    if N==1:
        y=x
        return y
    m=N//2
    k = np.arange(m)
    diag=np.exp(-2j * np.pi * k / N)
    p=1


    x_par=fft(x[::2])
    x_impar=diag * fft(x[1::2])

    y=np.concatenate((x_par+x_impar,x_par-x_impar))
    return y



N_values = [128, 256, 512, 1024, 2048, 4096, 8192]

timpi_dft = []
timpi_fft_custom = []
timpi_np_fft = []

for N in N_values:
    x = np.random.random(N)
        
    start = time.perf_counter()
    dft(x)
    timpi_dft.append(time.perf_counter() - start)
    
    start = time.perf_counter()
    fft(x)
    timpi_fft_custom.append(time.perf_counter() - start)

    start = time.perf_counter()
    np.fft.fft(x)
    timpi_np_fft.append(time.perf_counter() - start)


plt.figure(figsize=(10, 6))
plt.plot(N_values, timpi_dft, marker='o', label='DFT (Implementare proprie)')
plt.plot(N_values, timpi_fft_custom, marker='s', label='FFT (Implementare proprie)')
plt.plot(N_values, timpi_np_fft, marker='^', label='NumPy FFT')


plt.yscale('log')


plt.xscale('log', base=2)
plt.xticks(N_values, N_values)

plt.xlabel('Dimensiunea vectorului (N)')
plt.ylabel('Timpul de execuție (secunde) - Scară Logaritmică')
plt.title('Comparație Timp Execuție: DFT vs FFT vs NumPy FFT')
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)

plt.tight_layout()
plt.show()






    










