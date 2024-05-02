from charge import Charge, plot_field_line
import matplotlib.pyplot as plt
"""
One cool thing we could do for this problem is put our lists of lines
into some sort of text file, and then load them up. In this case,
I just called the plot_field_line function a ton of times.
"""
if __name__ == "__main__":
    charges = [Charge(7.5, 0, 1), Charge(-7.5, 0, -1)]
    y_extent = [-25, 25]
    x_extent = [-25, 25]
    plot_field_line((7.4, 0), (-7.5, 0),
                    x_extent,
                    y_extent,
                    charges,
                    0.01,
                    color="black")
    plot_field_line((7.5, 0.1), (-7.5, 0),
                    x_extent,
                    y_extent,
                    charges,
                    0.01,
                    color="black")
    plot_field_line((7.5, -0.1), (-7.5, 0),
                    x_extent,
                    y_extent,
                    charges,
                    0.01,
                    color="black")
    plot_field_line((7.45, 0.1), (-7.5, 0),
                    x_extent,
                    y_extent,
                    charges,
                    0.01,
                    color="black")
    plot_field_line((7.45, -0.1), (-7.5, 0),
                    x_extent,
                    y_extent,
                    charges,
                    0.01,
                    color="black")
    plot_field_line((7.55, 0.1), (-7.5, 0),
                    x_extent,
                    y_extent,
                    charges,
                    0.01,
                    color="black")
    plot_field_line((7.55, -0.1), (-7.5, 0),
                    x_extent,
                    y_extent,
                    charges,
                    0.01,
                    color="black")
    plot_field_line((-7.55, 0.1), (7.5, 0),
                    x_extent,
                    y_extent,
                    charges,
                    0.01,
                    propogation_direction="a",
                    color="black")
    plot_field_line((-7.55, -0.1), (7.5, 0),
                    x_extent,
                    y_extent,
                    charges,
                    0.01,
                    propogation_direction="a",
                    color="black")
    plot_field_line((-7.55, 0.0), (7.5, 0),
                    x_extent,
                    y_extent,
                    charges,
                    0.01,
                    propogation_direction="a",
                    color="black")
    plot_field_line((7.55, 0.0), (-7.5, 0),
                    x_extent,
                    y_extent,
                    charges,
                    0.01,
                    color="black")
    plt.title("Some Electric Field Lines in a Dipole")
    plt.show()
