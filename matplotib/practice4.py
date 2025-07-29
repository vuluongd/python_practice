import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1.5,1.5)
ax.set_ylim(-1.5,1.5)
point, = ax.plot([], [], 'ro')  


radius = 1
frames = 200
theta = np.linspace(0,2*np.pi,frames)

def update(i):
    x = radius*np.cos(theta[i])
    y = radius*np.sin(theta[i])
    point.set_data(x, y)
    return point,
ani = FuncAnimation(fig, update, frames=frames, interval=40, blit = True )

plt.title("chuyen dong hinh tron 2d")
plt.grid(True)
plt.show()