
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 100, 0.1)       # 1:99
x = np.linspace(1, 100, 90)

y1 = np.sin(x)/x
y2 = np.cos(x)/x * 10

fig, ax = plt.subplots(2, 1, sharex = True)

ax[0].plot(x, y1, label = 'y1', color = 'red')
ax[0].grid()
ax[0].legend()

ax[1].plot(x, y2, label = 'y2', color = 'limegreen')

# plt.savefig('my_plot_1.png')
plt.show()
