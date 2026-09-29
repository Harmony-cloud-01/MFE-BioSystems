# file: resonance_harmonics.py
# Purpose: Show amplitude spectra of three lightly-coupled resonators and their harmonic overlap.

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(7)

# Frequencies (Hz)
f = np.linspace(0.1, 200, 4000)

def lorentz(f, f0, Q, A=1.0):
    # magnitude of a second-order resonator (scaled)
    return A / np.sqrt(1 + Q**2*((f/f0) - (f0/f))**2)

# Three domains: "plasma", "MRI coil", "neural"
spec_plasma = lorentz(f, f0=60, Q=15, A=1.0)
spec_mri    = lorentz(f, f0=64, Q=25, A=0.9)
spec_neural = lorentz(f, f0=62, Q=8,  A=0.7)

# Harmonic content (add weak 2nd harmonic bumps)
spec_plasma += 0.15*lorentz(f, 120, Q=10, A=0.6)
spec_mri    += 0.10*lorentz(f, 128, Q=12, A=0.5)
spec_neural += 0.12*lorentz(f, 124, Q=9,  A=0.4)

# Normalise for plotting clarity
def nrm(x): 
    return x/np.max(x)

p, m, n = map(nrm, (spec_plasma, spec_mri, spec_neural))
overlap = p*m*n

plt.figure(figsize=(8.2, 4.4))
plt.plot(f, p, label='Plasma resonator')
plt.plot(f, m, label='MRI coil')
plt.plot(f, n, label='Neural circuit')
plt.plot(f, overlap, lw=2.0, label='Harmonic overlap (product)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Normalised amplitude')
plt.title('Resonance-Harmonic Spectrum and Cross-Domain Overlap')
plt.legend()
plt.tight_layout()
plt.savefig('fig_resonance_harmonics.png', dpi=300)
print('Saved fig_resonance_harmonics.png')
