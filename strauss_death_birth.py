import numpy as np
import matplotlib.pyplot as plt

def death_fn(grid):
    """
    Randomly selects a cell from the grid and returns its indices.

    Args:
    - grid: a numpy array representing the grid

    Returns:
    - a tuple containing the indices of the selected cell
    """
    i = np.random.randint(0, grid.shape[0])
    j = np.random.randint(0, grid.shape[1])
    return (i, j)

def birth_fn(h, w):
    """
    Generates a tuple of two random numbers between 0 and 1.
    This is the new point that will replace the dead point.

    Returns:
    tuple: A tuple of two random numbers between 0 and 1.
    """
    x = np.random.uniform(0, w+1E-40)
    y = np.random.uniform(0, h+1E-40)
    return (x, y)

def check_criteria(point_list, new_point, r0):
    """
    Check if a new point satisfies the Strauss process criteria.
    
    Args:
    - point_list (list): A list of existing points.
    - new_point (list): A new point to be checked.
    - r0 (float): The interaction radius.
    
    Returns:
    - dist_mask (numpy.ndarray): A boolean mask indicating whether the distance between
    the new point and existing points is less than r0.
    """
    points_array = np.array(point_list)
    dist = np.linalg.norm(points_array - new_point, axis=1)
    dist_mask = dist < r0
    return dist_mask

def pair_potential_fn(num_points_inside_r0, beta):
    """
    Calculates the pair potential function for a Strauss process.
    
    Args:
    - num_points_inside_r0 (int): The number of points inside the interaction radius.
    - beta (float): The interaction parameter.
    
    Returns:
    - float: The value of the pair potential function.
    """
    return np.exp(-beta * num_points_inside_r0)

def initial_grid(n_x, n_y, h, w):
    """
    Creates a uniform grid of points.

    Args:
        n (int): The number of points in each dimension of the grid.

    Returns:
        tuple: A tuple containing two arrays representing the x and y coordinates of the grid points.
    """
    x = np.linspace(0, w, n_x)
    y = np.linspace(0, h, n_y)
    xx, yy = np.meshgrid(x, y)
    return xx, yy

def simulation_step(r_s, beta, xx, yy, h, w):
    """
    Simulates a step in the Strauss process.

    Parameters:
    xx (numpy.ndarray): The x-coordinates of the points.
    yy (numpy.ndarray): The y-coordinates of the points.
    h (int): The height of the simulation area.
    w (int): The width of the simulation area.

    Returns:
    list: A list of the pair of points.
    """
    # kill a point
    dead_point_idx = death_fn(xx)
    # generate a new point
    new_point = birth_fn(h, w)
    print(f"The coordinate of the dead point is: ({xx[dead_point_idx]}, {yy[dead_point_idx]})")
    # ax.scatter(xx[dead_point_idx], yy[dead_point_idx], marker='x', c='r', s = marker_size)
    # replace the dead point with the new point
    xx[dead_point_idx] = new_point[0]
    yy[dead_point_idx] = new_point[1]
    # create a list of the pair of points
    points = list(zip(xx.flatten(), yy.flatten()))
    flag = True
    iteration_no = 0
    while flag:
        iteration_no += 1
        print(f"Iter: {iteration_no}")
        # check if the new point satisfies the Strauss process criteria
        dist_mask = check_criteria(points, new_point, r_s)
        # reshape dist_mask to the shape of xx
        dist_mask = dist_mask.reshape(xx.shape)
        number_of_points_inside_r0 = np.sum(dist_mask)
        phi = pair_potential_fn(number_of_points_inside_r0-1, beta)
        print("phi =", phi)
        # sample u from uniform distribution
        # u = np.random.uniform(0, 1)
        # we control how many pairs of points can have overlap
        u = 0.68
        print("u =", u)
        if u < phi:
            print("Accept")
            flag = False
        else:
            print("Reject")
            new_point = birth_fn(h, w)
            xx[dead_point_idx] = new_point[0]
            yy[dead_point_idx] = new_point[1]
        points = list(zip(xx.flatten(), yy.flatten()))
    return points

# if __name__ == "__main__":
    
#     # Number of points in a row or column of a uniform grid
#     n_x = 4
#     n_y = 4
#     # Interaction radius
#     r_s = 3
#     # Particle radius
#     r_i = 0.02
#     # Interaction parameter
#     beta = 0.4
#     # Marker size for plotting
#     marker_size = 30
#     # Number of simulation steps
#     sim_steps = 500
#     h = 27
#     w = 27
#     # create a uniform grid of points
#     xx, yy = initial_grid(n_x, n_y, h, w)
    
#     fig, ax = plt.subplots()
#     ax.set_xlim(-0.1, w+0.1)
#     ax.set_ylim(-0.1, h+0.1)
#     # draw a rectangle
#     rect = plt.Rectangle((0, 0), w, h, fill=False)
#     ax.add_patch(rect)

#     flag = True
#     for i in range(sim_steps):
#         points = simulation_step(r_s, beta, xx, yy, h, w)
#     plt.scatter(*zip(*points))
#     # plot a circle around each point with radius r_s/2
#     for point in points:
#         circle = plt.Circle(point, r_s/2, fill=False)
#         ax.add_artist(circle)
#     # equal aspect ratio
#     ax.set_aspect('equal', 'box')
#     plt.show()
#     # print the distance between points
#     points_array = np.array(points)
#     dist = np.linalg.norm(points_array - points_array[:, None], axis=-1)
#     print(f"distance: {dist}")
#     # save points to a file
#     # create a timestamp based name for the file
#     import time
#     timestamp = time.strftime("%Y%m%d-%H%M%S")
#     np.savetxt(f"strauss_points_{timestamp}.txt", points, fmt="%.6f")