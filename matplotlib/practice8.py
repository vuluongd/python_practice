import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 

file_path = "multi_position_sheet.xlsx"
xls = pd.ExcelFile(file_path)

chosen_sheets = input("nhập sheet: ").split(',')

chosen_sheets = [sheet.strip() for sheet in chosen_sheets if sheet.strip() in xls.sheet_names] 

trajectories = {}
for sheet in chosen_sheets:
    df = xls.parse(sheet)
    trajectories[sheet] = {
        'x':df['x'].values,
        'y':df['y'].values
    }
fig, ax = plt.subplots()
ax.set_title('Animation các sheet')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True)

all_x = [pt for traj in trajectories.values() for pt in traj['x']]
all_y = [pt for traj in trajectories.values() for pt in traj['y']]
ax.set_xlim(min(all_x)-1,max(all_x)+1)
ax.set_ylim(min(all_y)-1,max(all_y)+1)

lines = {}
points = {}
colors = ['r', 'g', 'b', 'm', 'c', 'orange', 'purple']

for i, sheet in enumerate(chosen_sheets):
    color = colors[i % len(colors)]
    (line,) = ax.plot([], [], '-', color=color, label=sheet)
    (point,) = ax.plot([], [], 'o', color=color)
    lines[sheet] = line
    points[sheet] = point 

def init():
    for sheet in chosen_sheets:
        lines[sheet].set_data([], [])
        points[sheet].set_data([], [])

    return list(lines.values())+list(points.values())

def update(frame):
    for sheet in chosen_sheets:
        x = trajectories[sheet]['x']
        y = trajectories[sheet]['y']
        if frame < len(x):
            lines[sheet].set_data(x[:frame], y[:frame])
            points[sheet].set_data(x[frame-1], y[frame-1])
    return list(lines.values()) + list(points.values())

max_frames = max(len(t['x']) for t in trajectories.values())
ani = FuncAnimation(fig, update, frames=max_frames, init_func=init, interval=50, blit=True)

ax.legend()
plt.show()
