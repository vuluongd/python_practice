from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
xdata, ydata = [], []
line, = ax.plot([], [], 'r-')

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1.5,1.5)
    return line,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    line.set_data(xdata,ydata)
    return line,

frames = np.linspace (0, 2*np.pi,128)
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)
plt.show()