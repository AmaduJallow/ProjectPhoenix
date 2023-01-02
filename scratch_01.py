import math
from collections import namedtuple


# Here we are using the brute force approach
def voronoi(point_values, width, height):
    # Initialize the data structures for the Voronoi diagram
    edges = []
    vertexIndices = {}

    # Iterate over all pairs of points
    for i, p1 in enumerate(point_values):
        for j, p2 in enumerate(point_values):
            if i == j:
                continue
            # Calculate the distance between the points
            dx = p1.x - p2.x
            dy = p1.y - p2.y
            d = math.sqrt(dx ** 2 + dy ** 2)
            # Calculate the midpoint between the points
            x = (p1.x + p2.x) / 2
            y = (p1.y + p2.y) / 2
            # Check if the midpoint is within the bounds of the diagram
            if x < 0 or x > width or y < 0 or y > height:
                continue
            # Add the midpoint to the vertex indices dictionary
            vertexIndices[(x, y)] = len(vertexIndices)
            # Add the edge to the edges list
            edges.append((i, j, d, x, y))

    return [edges, vertexIndices]


Point = namedtuple('Point', ['x', 'y'])

p_0 = Point(1, 2)
p_1 = Point(2, 1)
p_2 = Point(1, 1)
p_3 = Point(2, 3)
p_4 = Point(3, 4)
points = [p_0, p_1, p_2, p_3, p_4]

result = voronoi(points, 6, 5)
print(result[0])
print(result[1])
