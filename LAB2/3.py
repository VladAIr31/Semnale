import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap
import scipy
import sounddevice

f = 400

t = np.arange(0,1,step=1/1600)

semnal = np.sin(2 * np.pi * f * t)

n=4
fig, axs = plt.subplots(n)




f=800
t=np.arange(0,3,step=1/8000)
semnal = np.sin(2 * np.pi * f * t)




f=240
t=np.arange(0,1,step=1/8000)
semnal= (f*t) % 1


f=300 
t=np.arange(0,1,step=1/44100)
semnal= np.sign(np.sin(2*np.pi*f*t))



rate = int(44100)
scipy.io.wavfile.write('s1.wav', rate, semnal)

rate, x = scipy.io.wavfile.read('s1.wav')
fs=44100
sounddevice.play(x, fs)
sounddevice.wait()