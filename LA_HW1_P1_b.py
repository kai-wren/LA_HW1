import matplotlib.pyplot as plt
import numpy as np

def f1(t):
    return -2-2*t

def f2(t, k):
    return (4-k*t)/-2

t = np.arange(-5, 5, 0.05)
plt.subplot(131)
plt.plot(t, f1(t), 'r--', label='Equation 1')
plt.plot(t, f2(t, -4), 'b:', label="Equation 2")
plt.grid(True)
plt.title('k = -4')
plt.legend(bbox_to_anchor=(0.5, 0), loc='lower center')

plt.subplot(132)
plt.plot(t, f1(t), 'r', label='Equation 1')
plt.plot(t, f2(t, 8), 'b', label="Equation 2")
plt.grid(True)
plt.title('k = 8')
plt.legend(bbox_to_anchor=(0.5, 0), loc='lower center')
idx = np.argwhere(np.diff(np.sign(f1(t) - f2(t, 3)))).flatten()
plt.plot(t[idx], f1(t)[idx], 'ro')

plt.subplot(133)
plt.plot(t, f1(t),'r', label='Equation 1')
plt.plot(t, f2(t, -8), 'b', label="Equation 2")
plt.grid(True)
plt.title('k = -8')
plt.legend(bbox_to_anchor=(0.5, 0), loc='lower center')
idx = np.argwhere(np.diff(np.sign(f1(t) - f2(t, -9)))).flatten()
plt.plot(t[idx], f1(t)[idx], 'ro')

plt.show()