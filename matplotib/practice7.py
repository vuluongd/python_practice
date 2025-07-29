import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 

chosen_sheet = input("Nhap_sheet ")

file_path = "multi_position_sheet.xlsx"
xls= pd.ExcelFile(file_path)

df = xls.parse(chosen_sheet)
x_data = df['x'].values
y_data = df['y'].values

fig, ax = plt.subplots()
ax.set_xlim(min(x_data)-1,max(x_data)+1)
ax.set_ylim(min(y_data)-1,max(y_data)+1)
ax.set_title("chuyển động của {sheet_name}")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True)

line, = ax.plot([], [],'r-', lw = 2, label ='Đường đi')
point, = ax.plot([],[], 'bo', label='Drone')

def init():
    line.set_data([],[])
    point.set_data([],[])
    return line, point
def update(frame):
    line.set_data(x_data[:frame], y_data[:frame])
    point.set_data(x_data[frame-1], y_data[frame-1])
    return line, point
ani = FuncAnimation(fig, update, frames=len(x_data), init_func=init, interval=50, blit=True)
ax.legend()
plt.show()
