import numpy as np
import matplotlib.pyplot as plt

numbers = [3,5,7,8,9,2]

a = np.array(numbers)
print(type(a))

# x = np.arange(1, 10, 0.1)
x = np.linspace(1, 10, 91)
print(x)

y1 = np.sin(x)/x
y2 = np.cos(x)/x

plt.plot(x, y1, color='green')
plt.plot(x, y2)
plt.axhline(0, color='black', linewidth=1)
plt.legend(['Y1','Y2'])
plt.show()