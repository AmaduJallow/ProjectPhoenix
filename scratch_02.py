from collections import namedtuple


def voronoi(points, width, height):
    # Base case: return the edges for a single point
    if len(points) == 1:
        return [], {(points[0].x, points[0].y): 0}

    # Recursively compute the Voronoi diagrams for the left and right halves of the points
    leftPoints = points[:len(points) // 2]
    rightPoints = points[len(points) // 2:]
    leftEdges, leftVertices = voronoi(leftPoints, width, height)
    rightEdges, rightVertices = voronoi(rightPoints, width, height)

    # Merge the left and right diagrams
    edges = leftEdges + rightEdges
    vertices = leftVertices.copy()
    vertices.update(rightVertices)

    # Add the edges and vertices that connect the left and right diagrams
    midpoint = (leftPoints[-1].x + rightPoints[0].x) // 2
    edges.append((leftVertices[(midpoint, height)], rightVertices[(midpoint, 0)]))
    vertices[(midpoint, height)] = len(vertices)
    vertices[(midpoint, 0)] = len(vertices)

    return [edges, vertices]


Point = namedtuple('Point', ['x', 'y'])
p_0 = Point(1, 2)
p_1 = Point(2, 1)
p_2 = Point(1, 1)
p_3 = Point(2, 3)
points = [p_0, p_1, p_2, p_3]
result = voronoi(points, 2, 2)
print(result[1])
