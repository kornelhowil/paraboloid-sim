from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import odeint
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation

#constants
g = -9.81
k = 1
time = 30
v_0 = -1.5

#initial conditions
init0 = [-1.0, 0.0, 0.0, v_0]

#solving ODE
def par(init, t, g, k):
	x, v_x, y, v_y = init

	dydt=[	v_x, 
			(g*k*x-4*(k**2)*x*((v_x**2)+(v_y**2)))/(1+4*(k**2)*((x**2)+(y**2))),
			v_y,
			(g*k*y-4*(k**2)*y*((v_y**2)+(v_x**2)))/(1+4*(k**2)*((y**2)+(x**2)))]
	return dydt

t = np.linspace(0, time , time*60)
sol = odeint(par, init0, t, args=(g, k))

#generating z-axis data
height = []
for a, b in zip(sol[:, 0], sol[:, 2]):
	height.append(k*(a**2+b**2))

#########################################

#generating surface data
T = np.arange(0, 2*(np.pi), 0.01)
r = np.arange(0, 1.05, 0.01)
r, T = np.meshgrid(r, T)
#Parametrise it
x_surface = r*np.cos(T)
y_surface = r*np.sin(T)
z_surface = k*r**2

#########################################

fig = plt.figure()
ax = p3.Axes3D(fig)

def gen():
    for x, y, z in zip(sol[:, 0], sol[:, 2], height):
    	yield np.array([x, y, z])

def update(num, data, line, surf):
    line.set_data(data[:2, :num])
    line.set_3d_properties(data[2, :num])
    surf[0].remove()
    surf[0] = ax.plot_surface(x_surface, y_surface, z_surface, color='purple', alpha=0.3)

data = np.array(list(gen())).T
line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])
surf = [ax.plot_surface(x_surface, y_surface, z_surface, color='purple', alpha=0.3)]

# Setting the axes properties
ax.set_xlim3d([-1.1, 1.1])
ax.set_xlabel('x [m]')

ax.set_ylim3d([-1.1, 1.1])
ax.set_ylabel('y [m]')

ax.set_zlim3d([0.0, 1.1])
ax.set_zlabel('z [m]')

ani = animation.FuncAnimation(fig, update, fargs=(data, line, surf), frames=time*60, interval=16.6666, blit=False)
writervideo = animation.FFMpegWriter(fps=60) 
ani.save('plot.mp4', writer=writervideo)
plt.show()


