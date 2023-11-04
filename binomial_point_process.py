import numpy as np
import matplotlib.pyplot as plt
from point_process.plotting import plot_base

def gen_binomial_pp(N, h, w):
    x = np.random.uniform(0, w, N)
    y = np.random.uniform(0, h, N)
    return x, y

# if __name__ == "__main__":
#     # number of points
#     N = 10
#     # Simulation box size
#     x_max = 2
#     y_max = 1
#     # generate N random points using uniform distribution
#     x, y = gen_binomial_pp(N, x_max, y_max)
#     # plot the points
#     plot_base(x, y, x_max, y_max)