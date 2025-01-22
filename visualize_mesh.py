import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('mesh.dat')
x = data[:, 0]
y = data[:, 1]

plt.scatter(x, y, color='blue', label='Data Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of Mesh Data')
plt.legend()
plt.grid(True)
plt.show()
