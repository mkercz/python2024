# http://hplgit.github.io/num-methods-for-PDEs/doc/pub/wave/html/slides_wave-solarized.html

# 1D wave equation. Dirichlet conditions in 1D. Based on wave1b.py

import math
import numpy as np
import matplotlib.pyplot as plt

# Given mesh points as arrays x and t (x[i], t[j])
Nx, Nt, L, T, c = 20, 100, 1.0, 2.0, 1.0
t = np.linspace(0, T, num=Nt+1, dtype=float)   # t in [0,T]
x = np.linspace(0, L, num=Nx+1, dtype=float)   # x in [0,L]
dx = x[1] - x[0]
dt = t[1] - t[0]
r = (c*dt/dx)**2
print ( "r = {}".format(r) )
assert r < 1

u = np.empty( (Nx+1,Nt+1), dtype=float )  # all results

# initial condition, t=0, j=0
# initial shape of the string
# half of the string is at maximal displacement
u[:,0] = np.where(x < L/2, 1, 0)

u[0,0] = 0.0
u[Nx,0] = 0.0

assert abs(u[0,0]) < 1e-6 and abs(u[Nx,0]) < 1e-6

# boundary condition, x=0 and x=L
u[0,:] = 0.0
u[Nx,:] = 0.0

#for i in range(1,Nx):   # initial condition j=1
u[1:-1,1] = u[1:-1,0] + (r*0.5)*( u[:-2,0] -2*u[1:-1,0] + u[2:,0] )

# iteration/solution the linear algebraic equations
for j in range(1,Nt):
    u[1:-1,j+1] = -u[1:-1,j-1] +2*u[1:-1,j] + r*(u[:-2,j] -2*u[1:-1,j] + u[2:,j])

# visualization
plt.title("1D wave equation")
plt.xlabel("t")
plt.ylabel("x")

plt.imshow(u, cmap='hot', interpolation='nearest')

plt.colorbar()
plt.show()
