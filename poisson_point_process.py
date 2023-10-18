import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    #Simulation window box size
    x_min = 0
    x_max = 2
    y_min = 0
    y_max = 1
    xDelta = x_max - x_min
    yDelta = y_max - y_min #rectangle dimensions
    areaTotal = xDelta * yDelta
    
    # Point process parameters
    # Intensity
    lambda0=100
    
    #Simulate Poisson point process
    #Poisson number of points
    numbPoints = np.random.poisson(lambda0 * areaTotal)
    xx = xDelta * np.random.uniform(0, 1, numbPoints) + x_min
    yy = yDelta * np.random.uniform(0, 1, numbPoints) + y_min
    #Plotting
    plt.scatter(xx, yy)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Poisson point process")
    # set equal aspect ratio
    plt.gca().set_aspect('equal', adjustable='box')
    plt.gca().add_patch(plt.Rectangle((0, 0), x_max, y_max, fill=False))
    plt.show()
