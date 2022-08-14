import numpy as np
import matplotlib.pyplot as plt
import math

# values = np.array([[1, 2, 3, 4, 5, 6], [1, 2, 3, 6, 7]], dtype=object)
# print(values)
# print(values.shape)
# print(type(values))
# nums = np.ones((12, 4))
# print(nums.shape)
# nums = np.delete(nums, 0, axis = 0)
# print(nums)
# print(nums.shape)
#
x_values = np.linspace(0, 40, 20)
y_values = list(math.pow(i, 2) for i in range(1, 21))
plt.plot(x_values, y_values)
plt.show()
