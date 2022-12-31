from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

# Define a set of points
points = [[0, 0], [1, 0], [0, 1], [1, 1.5], [1, 1], [0.5, 0.5], [0.3, 0.5], [0.4, .3], [0.3, .7]]

# Compute the Voronoi diagram
vor = Voronoi(points)

# Plot the diagram
fig, ax = plt.subplots()
voronoi_plot_2d(vor, ax, show_vertices=True, line_colors='blue', line_width=1)
plt.show()
