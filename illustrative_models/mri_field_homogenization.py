# file: mri_field_homogenization.py
# Purpose: Compare |dB|/B0 maps with/without a passive shaping ring (toy model).

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Geometry (meters)
L = 0.20                    # field-of-view half-size (+/- L)
N = 401                     # grid points per axis
x = np.linspace(-L, L, N)
y = np.linspace(-L, L, N)
X, Y = np.meshgrid(x, y)
R = np.hypot(X, Y)

# Main coil: thin circular loop producing approximate "uniform" B0 + mild inhomogeneity
B0 = 1.0                    # Tesla (target)
# Add a smooth low-order spatial drift to mimic inhomogeneity
drift = 0.03*((X/L)**2 - 0.5*(Y/L)**2) + 0.01*np.sin(2*np.pi*X/(2*L))
B_no_filter = B0*(1.0 + drift)

# Passive shaping ring: simple corrective field model (first-order)
ring_radius = 0.11
S = 0.7                     # correction strength (0--1)
# Ring contribution: counter the drift more near the ring radius
ring_profile = np.exp(-((R - ring_radius)**2)/(2*(0.02**2)))
correction = -S * drift * ring_profile
B_with_filter = B0*(1.0 + drift + correction)

# Uniformity metric
def uniformity(B):
    return np.std(B)/np.mean(B)

u_no = uniformity(B_no_filter)
u_yes = uniformity(B_with_filter)

# Plot |dB|/B0 (%)
fig, ax = plt.subplots(1, 2, figsize=(9, 4.2), constrained_layout=True)
im0 = ax[0].imshow(100*np.abs(B_no_filter - B0)/B0, extent=[-L, L, -L, L], origin='lower')
ax[0].set_title(f'|dB|/B0 without ring (std/mean = {100*u_no:.1f}%)')
ax[0].set_xlabel('x (m)'); ax[0].set_ylabel('y (m)')
fig.colorbar(im0, ax=ax[0], fraction=0.046, pad=0.04, label='%')

im1 = ax[1].imshow(100*np.abs(B_with_filter - B0)/B0, extent=[-L, L, -L, L], origin='lower')
ax[1].set_title(f'|dB|/B0 with ring (std/mean = {100*u_yes:.1f}%)')
ax[1].set_xlabel('x (m)'); ax[1].set_ylabel('y (m)')
fig.colorbar(im1, ax=ax[1], fraction=0.046, pad=0.04, label='%')

plt.suptitle('MRI In-Plane Field Uniformity (Toy Model)', fontsize=12)
plt.savefig('fig_mri_uniformity.png', dpi=300)
print('Saved fig_mri_uniformity.png')
