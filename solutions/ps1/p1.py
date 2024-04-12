import numpy as np
import matplotlib.pyplot as plt
from charge import Charge

if __name__ == "__main__":
    x_grid, y_grid = np.meshgrid(np.arange(-25, 25), np.arange(-25, 25))
    charges = [Charge(-7.5, 0, -1), Charge(7.5, 0, -1)]
    potentials = np.sum(
        [charge.potential(x_grid, y_grid) for charge in charges], axis=0)

    plt.imshow(potentials, cmap='viridis', extent=(-25, 25, -25, 25), aspect=1)
    plt.colorbar()
    levels = np.linspace(-0.5, potentials.max(), 10)
    plt.contour(potentials,
                levels=levels,
                colors='black',
                linestyles='dotted',
                extent=(-25, 25, -25, 25))
    plt.show()
