import numpy as np
import matplotlib.pyplot as plt


print(np.__version__)

numbers = np.array(range(10))

print(type(numbers))
print(numbers)

print(numbers * 10)
print(numbers + numbers)

x = np.arange(0, 10, 0.1)
print(x)

x = np.linspace(0, 10, 16)
print(x)

print(x.ndim)
print(x.shape)
print(x.dtype)

m = x.reshape((4, 4)).astype('int')
print(m)

print(m.ndim)
print(m.shape)
print(m.dtype)

print(x)
print(x.round(2))

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.savefig('image.png')
plt.show()
