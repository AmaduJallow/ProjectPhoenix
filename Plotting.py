import numpy as np
import matplotlib.pyplot as plt
import matplotlib

x_value = np.linspace(0, 15, 16)

y_value = np.geomspace(0.1, 2000, 16)

# plt.plot(x_value, y_value, 'o--')
x = [4, 5, 3, 1, 6, 7]
# plt.plot(x)
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [(i ** 3 + 1) for i in x]
plt.plot(x, y, 'o--')

print(np.gradient(x[:2], y[:2]))
plt.show()
