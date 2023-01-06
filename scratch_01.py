import random
from collections import namedtuple

import matplotlib.pyplot as plotter

v_points = namedtuple('Point', ['x', 'y'])


def voronoi(point):
    edges_for_voronoi = []
    for k, point_1 in enumerate(point):
        for j, point_2 in enumerate(point):
            if k == j or k < 0 or j < 0 or point_1.x == point_2.x or point_1.y == point_2.y:
                continue
            bisector_x_value = (point_1.x + point_2.x) / 2
            bisector_y_value = (point_1.y + point_2.y) / 2
            edges_for_voronoi.append((bisector_x_value, bisector_y_value))

    return edges_for_voronoi, point


def pointGenerator(number_of_points):
    point_holder = []
    x = 0
    y = 0
    for i in range(number_of_points + 1):
        x = random.randint(1, number_of_points)
        y = random.randint(x, number_of_points)
        point_holder.append(v_points(x, y))

    return point_holder


def drawer(inputs):
    points_xs = []
    points_ys = []

    points_for_plot = inputs[0]
    x_intercepts = []
    y_intercepts = []
    for k in range(len(points_for_plot)):
        for j in range(k):
            if points_for_plot[k][0] == points_for_plot[j][0] and points_for_plot[k][1] == points_for_plot[j][1]:
                x_intercepts.append(points_for_plot[k][0])
                y_intercepts.append(points_for_plot[k][1])

    for point in inputs[1]:
        points_xs.append(point.x)
        points_ys.append(point.y)

    fig, ax = plotter.subplots()
    ax.scatter(points_xs, points_ys)
    ax.plot(x_intercepts, y_intercepts, linestyle='dashed', marker='x')
    plotter.show()
    return


# You can use the function to generate n numbers of points
points = pointGenerator(3)

# You can use this part here to pass points manually
points = [v_points(3, 4), v_points(4, 3), v_points(2, 3), v_points(2, 1)]
outputValues = voronoi(points)
drawer(outputValues)
