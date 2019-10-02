# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

def f1(t1, t2, a, b):
    return (1-a*t1)/b

def f2(t1, t2, a, b):
    return (2-a*t1-a*t2)/2

def f3(t1, t2, a, b):
    return (b-a*t2)

fig = plt.figure()
ax = fig.gca(projection='3d')

t1 = np.arange(-5, 5, 0.05)
t2 = np.arange(-5, 5, 0.05)
t1, t2 = np.meshgrid(t1, t2)
Z1 = f1(t1, t2, 1, 1)
Z2 = f2(t1, t2, 1, 1)
Z3 = f3(t1, t2, 1, 1)


surf = ax.plot_surface(t1, t2, Z1, linewidth=0, antialiased=False)
surf = ax.plot_surface(t1, t2, Z2, linewidth=0, antialiased=False)
surf = ax.plot_surface(t1, t2, Z3, linewidth=0, antialiased=False)

#plt.subplot(131)
#ax.plot_surface(t1, t2, (f1(t1, t2, 2, 2)))
#ax.plot_surface(t1, t2, (f2(t1, t2, 2, 2)))
#ax.plot_surface(t1, t2, (f2(t1, t2, 2, 2)))
#plt.grid(True)
#plt.title('label')
#plt.legend(bbox_to_anchor=(0.5, 0), loc='lower center')

plt.show()