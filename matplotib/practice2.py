import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(-10,10,100)

y1 = x**2
y2 = x**3

plt.plot(x,y1,label ='y=x^2')
plt.plot(x,y2,label = 'y=x^3')
plt.title("so sánh hai đồ thị")
plt.legend()
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.show()