# 1D heat/diffusion equation, based on heat1e.py

import math
import numpy as np
import matplotlib.pyplot as plt

D, Nx, Nt, L, T = 1.0, 40, 500, 1.0, 0.1
t = np.linspace(0, T, num=Nt+1, dtype=float)
x = np.linspace(0, L, num=Nx+1, dtype=float)
dx = x[1] - x[0]
dt = t[1] - t[0]
r = D*dt / (dx*dx)
print ( "r = {}".format(r) )
assert r < 0.5

u = np.empty( (Nx+1,Nt+1), dtype=float )  # macierz na wszystkie wyniki

# initial condition, t=0
u[8:13,0] = 1.0
u[18:23,0] = 1.0
u[28:33,0] = 1.0

# for initial conditions in the form of hot points, boundary conditions do most
# of the job

# boundary condition, x=0 and x=L=1

# both ends are cold, the rod is wrapped with some cold material
u[0,:] = 0.0
u[Nx,:] = 0.0

# iteration/solution the linear algebraic equations
for j in range(Nt):
    u[1:-1,j+1] = r*u[:-2,j] + (1-2*r)*u[1:-1,j] + r*u[2:,j]

# visualization
print ( u )
plt.title("1D heat equation")
plt.xlabel("time") # odwrotnie!
plt.ylabel("x")

plt.imshow(u[:,::5], cmap='hot', interpolation='hamming')

plt.colorbar()
plt.show()
