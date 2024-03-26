import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 101)

y1  = np.sin(x)/(x + 1)
y2  = y1 * 0.6

plt.plot(x, y1, label='y1')
plt.plot(x, y2, label='y2')

plt.grid()
plt.legend()

plt.show()
