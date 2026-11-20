import numpy as np
import matplotlib.pyplot as plt 

betas=[1,2,2000000001/1000000000,4]
for k,beta in enumerate (betas):
    t=np.linspace(-3,3,6000)

    sinccon=np.sinc(t*beta)**2


    frecvente=[1, 3/2, 2, 4]

    fig, axs=plt.subplots(2, 2, figsize=(10, 7))
    axs=axs.flatten()

    for i, fs in enumerate(frecvente):
        Ts=1/fs

        n_max = int(np.floor(3 / Ts))
        n = np.arange(-n_max, n_max + 1)
        ts = n * Ts
        x_esantionat = np.sinc(ts*beta)** 2

        x_reconstruit=np.zeros_like(t)
        for j in range(len(n)):
            x_reconstruit += x_esantionat[j] * np.sinc((t - n[j] * Ts) / Ts)      

        
        axs[i].plot(t, sinccon, color='black')
        axs[i].stem(ts, x_esantionat)
        axs[i].plot(t,x_reconstruit,linestyle='--',color='green')
        axs[i].set_title(f'fs = {fs} Hz (Ts = {Ts:.2f} s) beta={beta}')

    plt.tight_layout()
    plt.savefig(f"1{k}.pdf")
    plt.show()



