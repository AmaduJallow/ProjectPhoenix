import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay

# Define the points.
points = np.array(
    [[0, 3], [3, 4], [2, 1], [0.5, 0.6],
     [1.5, 2], [1, 2], [2, 0], [2, 1],
     [2, 2], [5, 6], [0, 5], [4, 4],
     [5, 1.5]])

# Compute the Voronoi diagram.
voronoi_diagram = Voronoi(points)

# Plot Delaunay Triangulation
triangulation = Delaunay(points)

# Plot the diagram.
fig, axis = plt.subplots()
voronoi_plot_2d(voronoi_diagram, axis, line_color='red', line_width=0.5)

# Customize the plot.
axis.set_xlim(0, 7.5)
axis.set_ylim(0, 7.5)
axis.set_title('Voronoi Diagram by Mariama Cham')
axis.set_xlabel('X Values')
axis.set_ylabel('Y Values')

# Add the point coordinates to the plot.
plt.plot(points[:, 0], points[:, 1], 'o', color='blue', markersize=2)
plt.triplot(points[:, 0], points[:, 1])
plt.show()
