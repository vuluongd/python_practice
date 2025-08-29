import control as ctrl
import matplotlib.pyplot as plt

# Define the transfer function G(s) = 1 / (s^2 + 3s + 2)
num = [1]
den = [1, 3, 2]
G = ctrl.TransferFunction(num,den)
print("Transfer Function G(s):")
print(G)
# Simulate the step response of the system
t, y = ctrl.step_response(G)
plt.figure()
plt.plot(t, y)
plt.title ('Step Response of G(s)')
plt.xlabel('Time(s)')
plt.ylabel('Response')
plt.grid()
plt.show()
# Plot the Bode plot of the system
plt.figure()
mag , phase , omega = ctrl.bode(G, dB = True)
plt.show()
# Calculate and print the poles and zeros of the system
poles = ctrl.pole(G)
zeros = ctrl.zero(G)
print("Poles of G(s):", poles)
print("Zeros of G(s):", zeros)
# Calculate and print the DC gain of the system
dc_gain = ctrl.dcgain(G)
print("DC Gain of G(s):", dc_gain)
# Perform a root locus analysis of the system
plt.figure()
ctrl.root_locus(G)
plt.title('Root Locus of G(s)')
plt.show()
# Simulate the response of the system to a custom input signal
t = [0, 1, 2, 3, 4, 5]
u = [0, 1, 0, -1, 0, 1]
t, y, x = ctrl.forced_response(G, T=t, U=u)
plt.figure()
plt.plot(t, y)
plt.title('Response to Custom Input Signal')            