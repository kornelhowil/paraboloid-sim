import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

def par(init, t, g, k):
	x, v_x, y, v_y = init

	dydt=[	v_x, 
			(g*k*x-4*(k**2)*x*((v_x**2)+(v_y**2)))/(1+4*(k**2)*((x**2)+(y**2))),
			v_y,
			(g*k*y-4*(k**2)*y*((v_y**2)+(v_x**2)))/(1+4*(k**2)*((y**2)+(x**2)))]
	return dydt

g = -9.81
k = 1

init0 = [-1.0, 0.0, 0.0, -3.132]

t = np.linspace(0, 1000 , 10000)
sol = odeint(par, init0, t, args=(g, k))

z = []
for a, b in zip(sol[:, 0], sol[:, 2]):
	z.append(k*(a**2+b**2))

print(sol[:, 0][3])
plt.plot(sol[:, 0], sol[:, 2], 'b', label='Trace 2D')
#plt.plot(t, sol[:, 1], 'g', label='v_x')
#plt.plot(t, sol[:, 2], 'r', label'y')
#plt.plot(t, sol[:, 3], 'y', label='v_y)')
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('y')
plt.title('k='+str(k))
plt.grid()
plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(sol[:, 0], sol[:, 2], z, label='Trace 3D')
plt.title('k='+str(k))
ax.legend(loc='best')
plt.show()
