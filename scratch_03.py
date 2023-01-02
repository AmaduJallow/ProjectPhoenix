from collections import namedtuple


class Site:
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y

    def __hash__(self):
        return self.index

    def __eq__(self, other):
        return self.index == other.index


def voronoi(points, width, height):
    # Base case: return the edges for a single point
    if len(points) == 1:
        return [], {points[0]: 0}

    # Recursively compute the Voronoi diagrams for the left and right halves of the points
    leftPoints = points[:len(points) // 2]
    rightPoints = points[len(points) // 2:]
    leftEdges, leftVertices = voronoi(leftPoints, width, height)
    rightEdges, rightVertices = voronoi(rightPoints, width, height)

    # Merge the left and right diagrams
    edges = leftEdges + rightEdges
    vertices = {}
    for vertex, index in leftVertices.items():
        vertices[vertex] = index
    for vertex, index in rightVertices.items():
        if vertex not in vertices:
            vertices[vertex] = len(vertices)

    # Add the edges and vertices that connect the left and right diagrams
    midpoint = (leftPoints[-1].x + rightPoints[0].x) // 2
    leftSite = Site(-1, midpoint, height)
    rightSite = Site(-1, midpoint, 0)
    edges.append((leftVertices[leftSite], rightVertices[rightSite]))
    vertices[leftSite] = len(vertices)
    vertices[rightSite] = len(vertices)

    return [edges, vertices]


Point = namedtuple('Point', ['x', 'y'])
p_0 = Point(1, 2)
p_1 = Point(2, 1)
p_2 = Point(1, 1)
p_3 = Point(2, 3)
points = [p_0, p_1, p_2, p_3]
result = voronoi(points, 2, 2)
print(result[1])
