import numpy as np


class Charge:

    def __init__(self, x: int, y: int, q: int):
        """
        Our charges will be on grid points. We'll set all constants to 1,
        and make our charges integer as well.
        """
        if x < 0 or y < 0:
            raise ValueError("x and y must be non-negative indices.")
        self.x = x
        self.y = y
        self.q = q

    def potential(self, x_grid: np.ndarray, y_grid: np.ndarray) -> np.ndarray:
        """
        Calculate the potential at each point in the grid.
        """
        if self.x >= x_grid.shape[0] or self.y >= y_grid.shape[1]:
            raise ValueError("Charge is outside the grid.")

        # calculate the distance from the charge to each point in the grid
        dx = x_grid - self.x
        dy = y_grid - self.y
        r = np.sqrt(dx**2 + dy**2)

        # calculate the potential at each point in the grid
        V = self.q / r
        return V
