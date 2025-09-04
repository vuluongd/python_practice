import matplotlib
matplotlib.use("module://mytkbackend")

import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6] , marker='o')
plt.title("My Tkinter Backend Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()