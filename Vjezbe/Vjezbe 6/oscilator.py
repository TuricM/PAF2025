import harmonic_oscillator as ho

o = ho.HarmonicOscillator(2,0,100,0.1)
o.oscillate(0.001)
o.plot_trajectory()
o.oscillate(0.01)
o.plot_trajectory()
o.oscillate(0.1)
o.plot_trajectory()