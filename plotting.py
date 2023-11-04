import matplotlib.pyplot as plt

def plot_base(x, y, **kwargs):
    plt.scatter(x, y)
    # plot the rectangle patch
    if 'w' in kwargs and 'h' in kwargs:
        w = kwargs['w']
        h = kwargs['h']
    plt.gca().add_patch(plt.Rectangle((0, 0), w, h, fill=False))
    # if there is a patch argument, plot it
    if 'patch' in kwargs:
        plt.gca().add_patch(plt.Rectangle((0.25, 0.25), 0.5, 0.5, fill=True, color='red', alpha=0.5))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Binomial point process")
    plt.show()
