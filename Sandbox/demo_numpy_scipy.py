import numpy as np
import matplotlib.pyplot as plt

# a = np.array([32, 34, 54, 67, 89, 9])
# a = np.arange(1, 20, dtype='float')
# a = np.linspace(1, 21, 11)
#
# print(a)
#
# print(a[3:6])
#
# print(a * 10)
#
# print([1, 2, 3] + [1, 2, 3])
# print(np.array([1,2,3]) + np.array([1,2,3]))
#
# print(a % 3 == 0)
# print(a[a % 3 == 0])
#
# print(a[[4,8,2,1]])

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.sin(x)/(x+1)

# plt.plot(x, y1, label='y1')
# plt.plot(x, y2, label='y2')
# plt.grid()
# plt.legend()
# plt.show()


from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(-0.5, 10, 1)  # len = 11
y = np.arange(4.5, 11, 1)  # len = 7

fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z)

plt.show()