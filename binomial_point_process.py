import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # number of points
    N = 10
    # Simulation box size
    x_max = 2
    y_max = 1
    # generate N random points using uniform distribution
    x = np.random.uniform(0, x_max, N)
    y = np.random.uniform(0, y_max, N)
    # plot the points
    plt.scatter(x, y)
    # plot the rectangle patch
    plt.gca().add_patch(plt.Rectangle((0, 0), x_max, y_max, fill=False))
    # plot a smaller rectangle patch inside the first one
    plt.gca().add_patch(plt.Rectangle((0.25, 0.25), 0.5, 0.5, fill=True, color='red', alpha=0.5))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Binomial point process")
    plt.show()
