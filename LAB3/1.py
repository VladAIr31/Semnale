import numpy as np 
import matplotlib.pyplot as plt
import math

N=8

n=np.arange(N)
k=n.reshape(N,1)


F=np.exp(-2j*np.pi*n*k/N)


fig, axes = plt.subplots(N, 2, figsize=(10, 12))

for i in range(N):
    axes[i, 0].stem(range(N), F[i, :].real)
    axes[i, 0].set_ylabel(f'Linia k={i}')
    if i == 0:
        axes[i, 0].set_title('Partea Reala')
        
    axes[i, 1].stem(range(N), F[i, :].imag)
    if i == 0:
        axes[i, 1].set_title('Partea Imaginara')

plt.tight_layout()


plt.savefig('1.pdf')
plt.show()


FH=np.conj(F).T

prod=np.dot(FH,F)

nIN=N*np.eye(N)

ans=np.allclose(prod,nIN)
print("Este F unitara ?")
print(ans)




