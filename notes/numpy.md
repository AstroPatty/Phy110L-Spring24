## Numpy Fundamentals

Numpy is a Python library that provides incredibly powerful tools for performing math with large arrays and matrices. It can speed up numerical Python code by multiple orders of magnitude, as long as you use it effectively. 

### Basic Rules

There are only two rules to remember when getting started with Numpy:

1. Don't loop over arrays
2. Use Numpy functions and operations whenever possible

For example, let's say you have a bunch of coordinates and you want to calculate the distance from each of these coordinates to some other point. This is the way you would do it with a loop:

```python
import numpy as np
import math

# I'll just create some random coordinates
x_coordinates = np.random.rand(1000)
y_coordinates = np.random.rand(1000)
# Let's compute the distance to the point (0.5, 0.5)
x,y = 0.5, 0.5
distances = []

for i in range(1000):
	x_coord = x_coordinates[i]
	y_coord = y_coordinates[i]

	dist = math.sqrt((x_coord - x)**2 + (y_coord - y)**2)
	distances.append(dist)
```

Compare that to the following code:

```python
import numpy as np

x_coordinates = np.random.rand(1000)
y_coordinates = np.random.rand(1000)
x,y = 0.5, 0.5


distances = np.sqrt((x_coordinates - x)**2 + (y_coordinates - y)**2)
```

Not only is this version of the code much shorter, it's also signifcantly faster. On my machine, the first version of the code takes around 0.43 seconds to run with 1 Million points. The second version of the code takes less than 0.01 seconds. Less than a half a second may not seem so bad, but when you're working with large datasets, complex algorithms, or you have to to run the calculation many times in a row, the time savings can be huge.

Let's unpack this a bit to see what's happening. When you take a numpy array and add or subtract a number, numpy adds/subtracts that number to every element in the array. So when we write `x_coordinates - x`, numpy subtracts `x` from every element in `x_coordinates`. You can think of this as a $dx$ array.

When we then square this array using `**2`. Again, numpy does this element-by-element (elementwise). We then add the $dx^2$ and $dy^2$ arrays together, and take the square root. k

Finally, we use numpy's square root function to take the square root of every element in the array. The resultant array is the euclidean distance from each point to the point `(0.5, 0.5)`.
Numpy can do lots of fun things with arrays of different shapes and sizes. This is known as "broadcasting." For example if you have a 10x5 array, and you add a 1x5 array to it, numpy will add the 1x5 array to every row in the 10x5 array.


## Using Builtin Numpy Functions

Numpy has s ton of built-in functions for doing math with arrays. One of them you've already seen, `numpy.sqrt`. If you have a mathematical operation you want to perform on an array, there's a good change numpy has a function for it. Here are some of the most common ones:

- `numpy.sqrt` - square root
- `numpy.exp` - exponential
- `numpy.log` - natural logarithm
- `numpy.dot` - dot product

It also includes ton of functions for changing and combining arrays in interesting ways:

- `numpy.concatenate` - concatenate two arrays
- `numpy.vstack` - stack arrays vertically
- `numpy.hstack` - stack arrays horizontally
- `numpy.split` - split an array into multiple arrays

and many more... You can find a full list of numpy functions in the [numpy documentation](https://numpy.org/doc/stable/reference/index.html).
