import numpy as np


class Charge:

    def __init__(self, x: int, y: int, q: int):
        """
        Our charges will be on grid points. We'll set all constants to 1,
        and make our charges integer as well.
        """
        self.x = x
        self.y = y
        self.q = q

    def potential(self, x_grid: np.ndarray, y_grid: np.ndarray) -> np.ndarray:
        """
        Calculate the potential at each point in the grid.
        """
        if x_grid.min() > self.x or x_grid.max() < self.x:
            raise ValueError("Charge x-coordinate outside of grid.")
        if y_grid.min() > self.y or y_grid.max() < self.y:
            raise ValueError("Charge y-coordinate outside of grid.")

        # calculate the distance from the charge to each point in the grid
        dx = x_grid - self.x
        dy = y_grid - self.y
        r = np.sqrt(dx**2 + dy**2)

        # calculate the potential at each point in the grid
        V = self.q / r
        return V

    def e_field(self, x, y):
        """
        Calculate the electric field at each point in the grid. Note
        it will also work if you give a single point
        """

        # calculate the distance from the charge to each point in the grid
        dx = x - self.x
        dy = y - self.y
        r = np.sqrt(dx**2 + dy**2)

        # calculate the electric field at each point in the grid
        Ex = self.q * dx / r**3
        Ey = self.q * dy / r**3
        return Ex, Ey
