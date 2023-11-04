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

def test_plot_base_with_rectangle():
    # Test plot_base with rectangle patch
    x = np.random.rand(10)
    y = np.random.rand(10)
    w = 0.5
    h = 0.5
    plot_base(x, y, w=w, h=h)
    plt.close()

def test_plot_base_with_patch():
    # Test plot_base with custom patch
    x = np.random.rand(10)
    y = np.random.rand(10)
    patch = Rectangle((0.25, 0.25), 0.5, 0.5, fill=True, color='red', alpha=0.5)
    plot_base(x, y, patch=patch)
    plt.close()