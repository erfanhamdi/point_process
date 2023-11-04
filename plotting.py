import matplotlib.pyplot as plt

def plot_base(x, y, h, w):
    plt.scatter(x, y)
    # plot the rectangle patch
    plt.gca().add_patch(plt.Rectangle((0, 0), w, h, fill=False))
    # plot a smaller rectangle patch inside the first one
    plt.gca().add_patch(plt.Rectangle((0.25, 0.25), 0.5, 0.5, fill=True, color='red', alpha=0.5))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Binomial point process")
    plt.show()
