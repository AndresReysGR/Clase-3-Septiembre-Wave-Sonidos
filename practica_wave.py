import sys
sys.path.insert(1, 'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate

from thinkdsp import read_wave
from thinkdsp import play_wave

import matplotlib.pyplot as plt

seno = SinSignal(freq=19940, amp=1, offset=0)

wave_seno = seno.make_wave(duration=1.0, start=0, framerate=44100)

decorate(xlabel="Tiempo (s)")
decorate(ylabel="Amplitud")

wave_seno.plot()

wave_seno.write("sonido.wav")

plt.show()