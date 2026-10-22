import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap
import scipy
import sounddevice

f1=400
f2=800

t=np.arange(0,1,step=1/44100)
semnal1= np.sin(2*np.pi*f1*t)
semnal2=np.sin(2*np.pi*f2*t)

semnal=np.concatenate((semnal1,semnal2))

rate = int(44100)
scipy.io.wavfile.write('s.wav', rate, semnal)

rate, x = scipy.io.wavfile.read('s.wav')
fs=44100
sounddevice.play(x, fs)
sounddevice.wait()