import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

df = pd.read_excel('position.xlsx')

fig, ax = plt.subplots()

ax.set_aspect('equal')
ax.set_xlim(-12, 12)
ax.set_ylim(-12, 12)
ax.set_title("Drone Flying in Circle")
ax.set_xlabel("X(m)")
ax.set_ylabel("Y(m)")

drone_point, = ax.plot([], [], 'ro', label='Drone')
path_line, = ax.plot([], [], 'b--', alpha=0.5, label='Path')
ax.legend()

xdata, ydata = [], []

def init():
    drone_point.set_data([], [])
    path_line.set_data([], [])
    return drone_point, path_line
def update(frame):
    x = df.loc[frame, 'x']
    y = df.loc[frame, 'y']
    xdata.append(x)
    ydata.append(y)
    drone_point.set_data(x,y)
    path_line.set_data(xdata, ydata)
    return drone_point, path_line
ani = FuncAnimation(fig, update, frames=len(df), init_func = init, blit=True, interval=50)
plt.show()