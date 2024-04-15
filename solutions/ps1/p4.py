from charge import Charge
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Problem 2, dipole

    x_grid, y_grid = np.meshgrid(np.arange(-25, 26), np.arange(-25, 26))
    charges = [Charge(-7.5, 0, -1), Charge(7.5, 0, 1)]
    potentials = np.sum(
        [charge.potential(x_grid, y_grid) for charge in charges], axis=0)
    e_field = np.gradient(potentials)
    # Note, numpy index ordering is (y,x), so to get angles that are consistent
    # with usual conventions, we need to do the opposite of what may be natural
    angles = np.degrees(np.arctan2(-e_field[0], -e_field[1]))
    plt.imshow(
        angles,
        extent=(-25, 25, -25, 25),
        cmap='twilight',
    )
    plt.colorbar()
    plt.title("Electric field direction for a dipole")
    plt.show()
    # Since we know the electric field goes like 1/r^3 for a dipole,
    # we expect the potential to go like 1/r^2.
