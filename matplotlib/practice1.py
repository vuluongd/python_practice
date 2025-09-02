import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(-10, 10 ,10)

y = x**2

plt.plot(x,y)
plt.title("Đồ thị y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
