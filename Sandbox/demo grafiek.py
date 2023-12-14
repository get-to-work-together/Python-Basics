import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 101)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.title('Nice!!')
plt.grid()
plt.show()