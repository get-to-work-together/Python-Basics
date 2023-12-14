import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.5)

print(x)
print(type(x))

m = np.linspace(0, 10, 16).reshape( (4,4) )

m = np.arange(1, 17).reshape( (4,4) )

print(m)
print(m.transpose())

print(m @ m) # dot product

print(x * 100)

x = np.linspace(1, 10, 391)
y = np.sin(x ** 2) / (x + 1)

print(y)

plt.plot(x, y)
plt.plot(x, y / 2)
plt.grid()
plt.axhline(0, color = 'gray', zorder = -1)
plt.legend(['A','B'])
plt.show()






