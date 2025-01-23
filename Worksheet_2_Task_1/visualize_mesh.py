import numpy as np
import matplotlib.pyplot as plt

# Load data from mesh.dat, skipping the header line
data = np.loadtxt('mesh.dat', delimiter=" ")

# Split data into X and Y columns
x = data[:, 0]
y = data[:, 1]

print(data)
# Plot the data
plt.scatter(x, y, color='blue', label='Data Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of Mesh Data')
plt.legend()
plt.grid(True)
plt.savefig('mesh_plot.png')  # Save the plot as an image file
plt.show()                   # Display the plot
