import numpy as np
import matplotlib.pyplot as plt

# numbers = [83,65,67,34,76,89,34,56,76,12,34]
#
#
# print(numbers)
# print(type(numbers))
#
# anumbers = np.array(numbers)
#
# print(anumbers)
# print(type(anumbers))

a = np.arange(1, 11, 0.5)
print(a)
print(a.dtype)

a = np.linspace(1, 11, 20)
print(a)
print(a.dtype)

print([1, 2, 3] + [4, 5, 6])
print(np.array([1, 2, 3]) + np.array([4, 5, 6]))


x = np.linspace(0, 10, 100)
y = np.sin(x)/(x + 1)

plt.plot(x, y, color='red')
plt.title('Graph')
plt.grid()
plt.show()