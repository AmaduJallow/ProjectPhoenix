from collections import namedtuple

import numpy as np

# We'll use the namedtuple 'Point' to represent the x and y coordinates of a point
Point = namedtuple('Point', ['x', 'y'])


def voronoi(point_values):
    # Find the bounding box for the points
    x_coords = [p.x for p in point_values]
    y_coords = [p.y for p in point_values]
    x_min = min(x_coords) - 1
    x_max = max(x_coords) + 1
    y_min = min(y_coords) - 1
    y_max = max(y_coords) + 1

    # Generate a grid of points to sample the Voronoi diagram
    grid = []
    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            p = Point(x, y)
            grid.append(p)

    # For each point in the grid, find the nearest point in the set of input points
    # and assign it to the Voronoi diagram
    diagram = {}
    for p in grid:
        nearest = min(point_values, key=lambda x: (x.x - p.x) ** 2 + (x.y - p.y) ** 2)
        if nearest in diagram:
            diagram[nearest].append(p)
        else:
            diagram[nearest] = [p]

    return diagram


p_0 = Point(1, 2)
p_1 = Point(2, 1)
p_2 = Point(1, 1)
p_3 = Point(2, 3)
p_4 = Point(3, 4)
p_5 = Point(2, 2)
points = [p_0, p_1, p_2, p_3, p_4, p_5]
result = voronoi(points)
print(result)
