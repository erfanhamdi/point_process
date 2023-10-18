import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    N = 1
    x_max = 2
    y_max = 1

    x = np.random.uniform(0, x_max, N)
    y = np.random.uniform(0, y_max, N)

    plt.scatter(x, y)
    # plot the rectangle patch
    plt.gca().add_patch(plt.Rectangle((0, 0), x_max, y_max, fill=False))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Uniform point process")
    plt.show()
