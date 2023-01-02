from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay
import numpy as np
import matplotlib.pyplot as plt

# Define a set of points
points = np.array([[1, 2], [2, 1], [1, 1], [2, 3]])

# Compute the Voronoi diagram
vor = Voronoi(points)
# Plot Delaunay Triangulation over the Voronoi diagram
triangulation = Delaunay(points)

# Plot the diagram
fig, axis = plt.subplots()
voronoi_plot_2d(vor, axis, show_vertices=True, line_colors='black', line_width=1)
# Customize the plot.

axis.set_title('Voronoi Diagram & Delaunay Triangulation')
axis.set_xlabel('X Values')
axis.set_ylabel('Y Values')
axis.set_xlim(-1, 6)
axis.set_ylim(-1, 6)

plt.plot(points[:, 0], points[:, 1], 'o', color='blue', markersize=4)
plt.triplot(points[:, 0], points[:, 1])
plt.show()
