import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = 2*x +1 + 0.1*np.random.randn(50)

plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()