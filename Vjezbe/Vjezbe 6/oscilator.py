import harmonic_oscillator as ho
import math as mt
import matplotlib.pyplot as plt
import numpy as np

v_0=2 #m/s
x_0=0 #m
k=100 #N/m
m=0.1 #kg
o = ho.HarmonicOscillator(v_0, x_0, k, m)
o.oscillate(0.001)
o.plot_trajectory()
o.oscillate(0.01)
o.plot_trajectory()
o.oscillate(0.1)
o.plot_trajectory()

T_a = 2*4*mt.atan(1)*mt.sqrt(m/k)
plt.axhline(y=T_a, color="red")
dt=np.linspace(0.001, 0.1, 200)
plt.scatter(dt, [o.period(el) for el in dt], color="black", lw=0.5)
plt.xlabel("dt [s]")
plt.ylabel("T [s]")
plt.title("Preciznost numerički dobivenog perioda u ovisnosti o vremenskom koraku dt")
plt.show()
