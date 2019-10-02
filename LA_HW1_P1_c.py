import matplotlib.pyplot as plt
import numpy as np

def f1(t, k):
    return (k+2*t)/4

def f2(t):
    return (-3-t)/-2

t = np.arange(-5, 5, 0.05)
plt.subplot(131)
plt.plot(t, f1(t, 6), 'r--', label='Equation 1')
plt.plot(t, f2(t), 'b:', label="Equation 2")
plt.grid(True)
plt.title('k = 6')
plt.legend(bbox_to_anchor=(0.5, 0), loc='lower center')

plt.subplot(132)
plt.plot(t, f1(t, 3), 'r', label='Equation 1')
plt.plot(t, f2(t), 'b', label="Equation 2")
plt.grid(True)
plt.title('k = 3')
plt.legend(bbox_to_anchor=(0.5, 0), loc='lower center')

plt.subplot(133)
plt.plot(t, f1(t, -9),'r', label='Equation 1')
plt.plot(t, f2(t), 'b', label="Equation 2")
plt.grid(True)
plt.title('k = -9')
plt.legend(bbox_to_anchor=(0.5, 0), loc='lower center')

plt.show()