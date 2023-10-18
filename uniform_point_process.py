import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # number of points
    N = 1
    # Simulation box size
    x_max = 2
    y_max = 1
    # generate random points using uniform distribution
    x = np.random.uniform(0, x_max, N)
    y = np.random.uniform(0, y_max, N)
    # plot the points
    plt.scatter(x, y)
    # plot the rectangle patch
    plt.gca().add_patch(plt.Rectangle((0, 0), x_max, y_max, fill=False))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Uniform point process")
    plt.show()
