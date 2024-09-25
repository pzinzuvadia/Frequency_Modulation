import numpy as np
import matplotlib.pyplot as plt

Am = float(input('Enter message amplitude: '))
Fm = float(input('Enter message frequency: '))
Ac = float(input('Enter carrier amplitude: '))
Fc = float(input('Enter carrier frequency: '))

m = float(input('Enter modulation index: '))

t = np.linspace(0,1,1000)

carrier = Ac*np.cos(2*np.pi*Fc*t)
message = Am*np.cos(2*np.pi*Fm*t)
FM_modulated_signal= Ac*np.cos(2*np.pi*Fc*t + m*np.sin(2*np.pi*Fm*t))

plt.subplot(3,1,1)
#plt.title('Amplitude Modulation')
plt.title('Frequency Modulation')
plt.plot(message,'g')
plt.ylabel('Amplitude')
plt.xlabel('Message signal')

plt.subplot(3,1,2)
plt.plot(carrier, 'r')
plt.ylabel('Amplitude')
plt.xlabel('Carrier signal')

plt.subplot(3,1,3)
plt.plot(FM_modulated_signal, color="purple")
plt.ylabel('Amplitude')
#plt.xlabel('AM signal')
plt.xlabel('FM Signal')
plt.subplots_adjust(hspace=1)
plt.rc('font', size=15)
fig = plt.gcf()
fig.set_size_inches(16 ,9)
