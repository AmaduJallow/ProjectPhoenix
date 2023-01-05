import math
from collections import namedtuple
import matplotlib.pyplot as plt


# Here we are using the brute force approach
def voronoi(point_values):
    # Initialize the data structures for the Voronoi diagram
    edges = []
    vertexIndices = {}

    # Iterate over all pairs of points
    for i, p1 in enumerate(point_values):
        for j, p2 in enumerate(point_values):
            if i == j:
                continue
            # Calculate the distance between the points
            dx = abs(p1.x - p2.x)
            dy = abs(p1.y - p2.y)
            d = math.sqrt(dx ** 2 + dy ** 2)
            # Calculate the midpoint between the points
            x = (p1.x + p2.x) / 2
            y = (p1.y + p2.y) / 2
            # Check if the midpoint is within the bounds of the diagram
            if x < 0 or y < 0:
                continue
            # Add the midpoint to the vertex indices dictionary
            vertexIndices[(x, y)] = len(vertexIndices)
            # Add the edge to the edges list
            edges.append((d, x, y))

    return [edges, vertexIndices, point_values]


def generate_diagram(result):
    voronoi_x_bisector = []
    voronoi_y_bisector = []
    points_x_values = []
    points_y_values = []

    datapoints = result[0]

    for i in range(len(datapoints)):
        for j in range(i):
            if datapoints[i][1] == datapoints[j][1] and datapoints[i][2] == datapoints[j][2]:
                voronoi_x_bisector.append(datapoints[j][1])
                voronoi_y_bisector.append(datapoints[j][2])
            else:
                continue

    for point in result[2]:
        points_x_values.append(point.x)
        points_y_values.append(point.y)

    # Plot a graph
    fig, axis = plt.subplots()
    axis.set_title('Voronoi Diagram')
    axis.set_xlabel('X Values')
    axis.set_ylabel('Y Values')
    axis.set_xlim(0, 4)
    axis.set_ylim(0, 4)
    axis.scatter(points_x_values, points_y_values, linewidth=2)
    axis.plot(voronoi_x_bisector, voronoi_y_bisector, color='green', linestyle='dashed', marker='x',
              markerfacecolor='blue', markersize=5)
    plt.show()


Point = namedtuple('Point', ['x', 'y'])
p_0 = Point(1, 1)
p_1 = Point(1, 2)
p_2 = Point(2, 2)
points = [p_0, p_1, p_2, Point(2, 1)]
outputValues = voronoi(points)
generate_diagram(outputValues)
