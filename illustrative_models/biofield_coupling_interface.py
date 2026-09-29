# file: biofield_coupling_interface.py
# Purpose: Solve div(sigma*grad(phi))=0 on a square with two conductivity regions; visualise field lines.

import numpy as np
import matplotlib.pyplot as plt

# Grid
N = 200
L = 1.0
x = np.linspace(-L, L, N)
y = np.linspace(-L, L, N)
X, Y = np.meshgrid(x, y)

# Conductivity map: left = tissue (sigma1), right = prosthetic shell (sigma2)
sigma1, sigma2 = 1.0, 4.0
sigma = np.where(X < 0.0, sigma1, sigma2)

# Boundary conditions: phi = +1 V on top edge, phi = 0 V on bottom edge; insulated sides
phi = np.zeros((N, N))
phi[-1, :] = 1.0
phi[ 0, :] = 0.0

# Iterative finite-difference (weighted Jacobi)
w = 0.8
for it in range(1800):
    phi_new = phi.copy()

    # Effective sigma at faces (harmonic mean)
    sig_xp = 2*sigma[:, 1:]*sigma[:, :-1]/(sigma[:, 1:]+sigma[:, :-1])
    sig_xm = sig_xp.copy()
    sig_yp = 2*sigma[1:, :]*sigma[:-1, :]/(sigma[1:, :]+sigma[:-1, :])
    sig_ym = sig_yp.copy()

    px = (sig_xp[1:-1, 1:]   * phi[1:-1, 2:] +
          sig_xm[1:-1, 0:-1] * phi[1:-1, 0:-2])
    py = (sig_yp[1:, 1:-1]   * phi[2:, 1:-1] +
          sig_ym[0:-1, 1:-1] * phi[0:-2, 1:-1])

    denom = (sig_xp[1:-1, 1:] + sig_xm[1:-1, 0:-1] +
             sig_yp[1:, 1:-1] + sig_ym[0:-1, 1:-1] + 1e-12)

    phi_new[1:-1, 1:-1] = (px + py)/denom

    # Neumann on sides (copy neighbours)
    phi_new[:, 0]  = phi_new[:, 1]
    phi_new[:, -1] = phi_new[:, -2]

    phi = w*phi_new + (1-w)*phi

# Electric field E = -grad(phi)
Ex, Ey = np.gradient(-phi, x, y)

# Plot potential and streamlines
fig, ax = plt.subplots(1, 2, figsize=(9.2, 4.2), constrained_layout=True)
im0 = ax[0].imshow(phi, extent=[-L, L, -L, L], origin='lower', cmap='viridis')
ax[0].set_title('Potential phi across tissue--prosthetic interface')
ax[0].set_xlabel('x'); ax[0].set_ylabel('y')
fig.colorbar(im0, ax=ax[0], fraction=0.046, pad=0.04, label='V')

speed = np.hypot(Ex, Ey)
ax[1].streamplot(x, y, Ex, Ey, density=1.6, linewidth=1.0, color=speed, cmap='plasma')
ax[1].axvline(0.0, color='k', lw=1.0, ls='--', label='interface')
ax[1].legend()
ax[1].set_title('Field lines (|E|) and interface')
ax[1].set_xlabel('x'); ax[1].set_ylabel('y')

plt.savefig('fig_biofield_interface.png', dpi=300)
print('Saved fig_biofield_interface.png')
