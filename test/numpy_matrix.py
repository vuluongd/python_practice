import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data.csv")

t = data["time"].values
ax = data["ax"].values
ay = data["ay"].values
A = np.array [1, 2, 3]

