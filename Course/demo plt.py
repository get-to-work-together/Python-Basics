import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 10, 100)
y = np.sin(x)

plt.savefig('my_image.png')
plt.plot(x, y)
plt.show()