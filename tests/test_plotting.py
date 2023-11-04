import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
from point_process.plotting import plot_base

def test_plot_base():
    # Test basic functionality with no kwargs
    x = np.random.rand(10)
    y = np.random.rand(10)
    plot_base(x, y)
    plt.close()