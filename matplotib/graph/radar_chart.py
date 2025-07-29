import matplotlib.pyplot as plt
import numpy as np

labels = np.array(['A', 'B', 'C', 'D', 'E'])
data = np.array([4, 5, 3, 4, 2])

angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))

plt.polar(angles, data, marker='o')
plt.fill(angles, data, alpha=0.25)
plt.title('Radar chart')
plt.show()
