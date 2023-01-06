from collections import namedtuple
import matplotlib.pyplot as plt

v_points = namedtuple('Point', ['x', 'y'])


def voronoi(input_values):
    edges_for_voronoi = []
    for k, point_1 in enumerate(input_values):
        for j, point_2 in enumerate(input_values):
            if k == j or k < 0 or j < 0 or point_1.x == point_2.x or point_1.y == point_2.y:
                continue
            bisector_x_value = (point_1.x + point_2.x) / 2
            bisector_y_value = (point_1.y + point_2.y) / 2
            edges_for_voronoi.append((bisector_x_value, bisector_y_value))

    return edges_for_voronoi, input_values


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

    fig, ax = plt.subplots()
    ax.scatter(points_xs, points_ys)
    ax.plot(x_intercepts, y_intercepts, linestyle='dashed', marker='x')
    plt.show()
    return


points = [v_points(3, 4), v_points(4, 3), v_points(2, 3), v_points(2, 1)]
outputValues = voronoi(points)
drawer(outputValues)
