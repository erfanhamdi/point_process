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

def birth_fn():
    """
    Generates a tuple of two random numbers between 0 and 1.
    This is the new point that will replace the dead point.

    Returns:
    tuple: A tuple of two random numbers between 0 and 1.
    """
    x = np.random.uniform(0, 1)
    y = np.random.uniform(0, 1)
    return (x, y)
    
import numpy as np

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

def initial_grid(n):
    """
    Creates a uniform grid of points.

    Args:
        n (int): The number of points in each dimension of the grid.

    Returns:
        tuple: A tuple containing two arrays representing the x and y coordinates of the grid points.
    """
    x = np.linspace(0, 1, n)
    y = np.linspace(0, 1, n)
    xx, yy = np.meshgrid(x, y)
    return xx, yy

def simulation_step(xx, yy):
    # kill a point
    dead_point_idx = death_fn(xx)
    # generate a new point
    new_point = birth_fn()
    print(f"The coordinate of the dead point is: ({xx[dead_point_idx]}, {yy[dead_point_idx]})")
    # ax.scatter(xx[dead_point_idx], yy[dead_point_idx], marker='x', c='r', s = marker_size)
    # replace the dead point with the new point
    xx[dead_point_idx] = new_point[0]
    yy[dead_point_idx] = new_point[1]
    # create a list of the pair of points
    points = list(zip(xx.flatten(), yy.flatten()))
    flag = True
    while flag:
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
            new_point = birth_fn()
            xx[dead_point_idx] = new_point[0]
            yy[dead_point_idx] = new_point[1]
        points = list(zip(xx.flatten(), yy.flatten()))
    return points

if __name__ == "__main__":
    
    # Number of points in a row or column of a uniform grid
    n = 5
    # Interaction radius
    r_s = 0.05
    # Particle radius
    r_i = 0.02
    # Interaction parameter
    beta = 0.4
    # Marker size for plotting
    marker_size = 30
    # Number of simulation steps
    sim_steps = 100

    # create a uniform grid of points
    xx, yy = initial_grid(n)
    
    fig, ax = plt.subplots()
    
    flag = True
    for i in range(sim_steps):
        points = simulation_step(xx, yy)
        # set the limits of the plot
        # ax.set_xlim([-0.2, 1.2])
        # ax.set_ylim([-0.2, 1.2])
        # # kill a point
        # dead_point_idx = death_fn(xx)
        # # generate a new point
        # new_point = birth_fn()
        # print(f"The coordinate of the dead point is: ({xx[dead_point_idx]}, {yy[dead_point_idx]})")
        # ax.scatter(xx[dead_point_idx], yy[dead_point_idx], marker='x', c='r', s = marker_size)
        # # replace the dead point with the new point
        # xx[dead_point_idx] = new_point[0]
        # yy[dead_point_idx] = new_point[1]
        # # create a list of the pair of points
        # points = list(zip(xx.flatten(), yy.flatten()))
        # while flag:
        #     # check if the new point satisfies the Strauss process criteria
        #     dist_mask = check_criteria(points, new_point, r_s)
        #     # reshape dist_mask to the shape of xx
        #     dist_mask = dist_mask.reshape(xx.shape)
        #     number_of_points_inside_r0 = np.sum(dist_mask)
        #     phi = pair_potential_fn(number_of_points_inside_r0-1, beta)
        #     print("phi =", phi)
        #     # sample u from uniform distribution
        #     # u = np.random.uniform(0, 1)
        #     # we control how many pairs of points can have overlap
        #     u = 0.68
        #     print("u =", u)
        #     if u < phi:
        #         print("Accept")
        #         flag = False
        #     else:
        #         print("Reject")
        #         new_point = birth_fn()
        #         xx[dead_point_idx] = new_point[0]
        #         yy[dead_point_idx] = new_point[1]
        #     points = list(zip(xx.flatten(), yy.flatten()))
        # ax.scatter(xx[dist_mask], yy[dist_mask], c='g', s = marker_size)
        # draw a circle of radius r_s/2 around the new point
        # draw circle of radius r_i around all other points
        # for point in points:
        #     circle_i = plt.Circle(point, r_s/2, color='b', fill=False)
        #     fig.gca().add_patch(circle_i)
        # circle = plt.Circle(new_point, r_s/2, color='r', fill=False)
        # fig.gca().add_patch(circle)
        # ax.scatter(xx[~dist_mask], yy[~dist_mask], c='b', s = marker_size)
        # ax.set_title(f"Step {i}")
        # # equal aspect ratio
        # fig.gca().set_aspect('equal', adjustable='box')
        # # fig.savefig("figs/strauss_death_birth_step_00" + str(i) + ".jpg")
        # ax.cla()
        # flag = True
    plt.scatter(*zip(*points))
    plt.show()
    # plt.figure()
    # # plot the grid
    # import plotly.express as px
    # fig = px.scatter(x=xx.flatten(), y=yy.flatten())
    # # make equal aspect ratio
    # fig.update_xaxes(range=[0, 1], constrain='domain')
    # fig.show()


