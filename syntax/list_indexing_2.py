import numpy as np

list = [np.array([0.0, 0.0, 0.0])]

for i in range(5):
    new_pos = list[-1] + np.random.uniform(-0.5, 0.5, size = 3)
    list.append(new_pos)
    print(f"step {i+1}")
    print("prev :", list[-2])
    print("curr :", list[-1])
