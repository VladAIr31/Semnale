import numpy as np 
import matplotlib.pyplot as plt
import csv
x = np.genfromtxt('Train.csv', delimiter=',')
esantioane=x[1:,0]
valori=x[1:,2]
#1 1/3600 hz
#2 18288
#3  1/3600/2-> 1/7200

plt.plot(esantioane, valori) 

plt.xlabel('Eșantioane')
plt.ylabel('Valori ')
plt.title('Reprezentare Eșantioane vs. Valori')
plt.show()
Fs = 1/3600 #hz
media=np.mean(valori)
valori=valori-media
N = len(valori)

X = np.fft.fft(valori)
X= np.abs(X / N) 

X = X[:N//2]
X[0]=0

f = Fs * np.linspace(0, N//2, N//2) / N


plt.figure()
plt.plot(f, X)
plt.xlabel('Frecvențe')
plt.ylabel('Amplitudine')
plt.title('Transformata Fourier a semnalului')
plt.show()


