from charge import Charge
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Problem 2, dipole

    x_grid, y_grid = np.meshgrid(np.arange(-25, 25), np.arange(-25, 25))
    charges = [Charge(-7.5, 0, -1), Charge(7.5, 0, 1)]
    potentials = np.sum(
        [charge.potential(x_grid, y_grid) for charge in charges], axis=0)
    e_field = np.gradient(potentials)
    angles = np.degrees(np.arctan2(e_field[1], e_field[0]))
    plt.imshow(angles,
               extent=(-25, 25, -25, 25),
               cmap='twilight',
               origin='lower')
    plt.colorbar()
    plt.title("Electric field direction for a dipole")
    plt.show()
    # Since we know the electric field goes like 1/r^3 for a dipole,
    # we expect the potential to go like 1/r^2.
