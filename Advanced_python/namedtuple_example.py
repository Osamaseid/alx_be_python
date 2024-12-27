from collections import namedtuple

# Define a named tuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p)  # Outputs: Point(x=10, y=20)
print(p.x, p.y)  # Outputs: 10 20