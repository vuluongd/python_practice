import control as ctrl
import matplotlib.pyplot as plt

# Define the transfer function G(s) = 1 / (s^2 + 3s + 2)
num = [1]
den = [1, 3, 2]
G = ctrl.TransferFunction(num,den)
print("Transfer Function G(s):")
print(G)