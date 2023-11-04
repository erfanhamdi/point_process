import numpy as np
import matplotlib.pyplot as plt
# from point_process.plotting import plot_base
# from plotting import plot_base
def gen_poisson_pp(lambda0, w, h):
    #Poisson number of points
    numbPoints = np.random.poisson(lambda0 * h * w)
    xx = w * np.random.uniform(0, 1, numbPoints)
    yy = h * np.random.uniform(0, 1, numbPoints)
    return xx, yy

# if __name__ == "__main__":
    #Simulation window box size
    # x_min = 0
    # x_max = 2
    # y_min = 0
    # y_max = 1
    #Plotting the points
    # xx, yy = gen_poisson_pp(2, x_max, y_max)
    # plot_base(xx, yy, w=x_max, h=y_max)    
    # plt.scatter(xx, yy)
    # plt.xlabel("x")
    # plt.ylabel("y")
    # plt.title("Poisson point process")
    # # set equal aspect ratio
    # plt.gca().set_aspect('equal', adjustable='box')
    # plt.gca().add_patch(plt.Rectangle((0, 0), x_max, y_max, fill=False))
    # plt.show()