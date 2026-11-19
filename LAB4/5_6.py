import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

fs, semnal = wavfile.read('vocale.wav')

if semnal.ndim > 1:
    semnal = semnal[:, 0]

N = len(semnal)

dim_grup = int(0.01 * N)
pas = dim_grup // 2  

coloane_fft = []

for start in range(0, N - dim_grup + 1, pas):
    grup = semnal[start : start + dim_grup]
    
    fft_grup = np.fft.fft(grup)
    
    fft_jumatate = fft_grup[:dim_grup // 2]
    
    coloane_fft.append(np.abs(fft_jumatate))

matrice_spectrograma = np.column_stack(coloane_fft)

spectrograma_db = 10 * np.log10(matrice_spectrograma**2 + 1e-10)

plt.figure(figsize=(10, 6))
plt.imshow( spectrograma_db,aspect='auto',origin='lower',cmap='inferno',extent=[0, N / fs, 0, fs / 2])
plt.colorbar(label='Putere (dB)')
plt.xlabel('Timp (s)')
plt.ylabel('Frecvență (Hz)')
plt.title('Spectrograma vocalelor (a, e, i, o, u)')
plt.tight_layout()
plt.savefig("6.pdf")
plt.show()