import numpy as np
import matplotlib.pyplot as plt

def death_fn(grid):
    # select a random index from the grid
    i = np.random.randint(0, grid.shape[0])
    j = np.random.randint(0, grid.shape[1])
    return (i, j)

def birth_fn():
    # draw a uniform random number between 0 and 1
    x = np.random.uniform(0, 1)
    y = np.random.uniform(0, 1)
    return (x, y)
    
def check_criteria(point_list, new_point, r0):
    points_array = np.array(point_list)
    dist = np.linalg.norm(points_array - new_point, axis=1)
    dist_mask = dist < r0
    return dist_mask

def pair_potential_fn(num_points_inside_r0, beta):
    return np.exp(-beta * num_points_inside_r0)

if __name__ == "__main__":
    
    n = 15
    r_s = 0.05
    r_i = 0.02
    beta = 0.4

    marker_size = 30

    # create a uniform grid of points
    x = np.linspace(0, 1, n)
    y = np.linspace(0, 1, n)
    xx, yy = np.meshgrid(x, y)
    # plot the grid
    flag = True
    fig, ax = plt.subplots()
    # plt.figure()
    for i in range(150):
        ax.set_xlim([-0.2, 1.2])
        ax.set_ylim([-0.2, 1.2])
        # plt.scatter(xx, yy, marker='x', c='r', s=marker_size)
        dead_point_idx = death_fn(xx)
        new_point = birth_fn()
        print(xx[dead_point_idx], yy[dead_point_idx])
        ax.scatter(xx[dead_point_idx], yy[dead_point_idx], marker='x', c='r', s = marker_size)
        # replace the dead point with the new point
        xx[dead_point_idx] = new_point[0]
        yy[dead_point_idx] = new_point[1]
        # print(xx[dead_point_idx], yy[dead_point_idx])
        # ax.scatter(xx, yy)
        # create a list of the pair of points
        points = list(zip(xx.flatten(), yy.flatten()))
        while flag:
            dist_mask = check_criteria(points, new_point, r_s)
            # reshape dist_mask to the shape of xx
            dist_mask = dist_mask.reshape(xx.shape)
            number_of_points_inside_r0 = np.sum(dist_mask)
            phi = pair_potential_fn(number_of_points_inside_r0-1, beta)
            print("phi =", phi)
            # sample u from uniform distribution
            # u = np.random.uniform(0, 1)
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
        ax.scatter(xx[dist_mask], yy[dist_mask], c='g', s = marker_size)
        # draw a circle of radius r0 around the new point
        # draw circle of radius r_i around all other points
        for point in points:
            circle_i = plt.Circle(point, r_s/2, color='b', fill=False)
            fig.gca().add_patch(circle_i)
        circle = plt.Circle(new_point, r_s/2, color='r', fill=False)
        fig.gca().add_patch(circle)
        ax.scatter(xx[~dist_mask], yy[~dist_mask], c='b', s = marker_size)
        ax.set_title(f"Step {i}")
        # equal aspect ratio
        fig.gca().set_aspect('equal', adjustable='box')
        fig.savefig("strauss_death_birth_step_00" + str(i) + ".jpg")
        # plt.show()
        ax.cla()
        flag = True
    
    plt.figure()
    # plot the grid
    import plotly.express as px
    fig = px.scatter(x=xx.flatten(), y=yy.flatten())
    # make equal aspect ratio
    fig.update_xaxes(range=[0, 1], constrain='domain')
    fig.show()


