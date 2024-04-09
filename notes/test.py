import numpy as np
import math
import time

n_points = 1_000_000
# I'll just create some random coordinates
x_coordinates = np.random.rand(n_points)
y_coordinates = np.random.rand(n_points)
# Let's compute the distance to the point (0.5, 0.5)
x, y = 0.5, 0.5
distances = []
start = time.time()
for i in range(n_points):
    x_coord = x_coordinates[i]
    y_coord = y_coordinates[i]

    dist = math.sqrt((x_coord - x)**2 + (y_coord - y)**2)
    distances.append(dist)
end = time.time()
print("Time taken using loop: ", end - start)

start = time.time()
distances = np.sqrt((x_coordinates - x)**2 + (y_coordinates - y)**2)
end = time.time()

print("Time taken using numpy: ", end - start)
