
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_data():
    x = np.random.randn(100)
    y = np.random.randn(100)

    plt.figure(figsize=(14, 6))

    # Scatter plot
    plt.subplot(2, 3, 1)
    plt.scatter(x, y)
    plt.title("Scatter Plot")

    # Box plot
    plt.subplot(2, 3, 2)
    sns.boxplot(x=x)
    plt.title("Box Plot")

    # Heatmap
    data = np.random.rand(10, 10)
    plt.subplot(2, 3, 3)
    sns.heatmap(data, cmap='viridis')
    plt.title("Heatmap")

    # Contour plot
    plt.subplot(2, 3, 4)
    X, Y = np.meshgrid(np.linspace(-3, 3, 100), np.linspace(-3, 3, 100))
    Z = np.sin(X**2 + Y**2)
    contour = plt.contourf(X, Y, Z, cmap='coolwarm')
    plt.colorbar(contour)
    plt.title("Contour Plot")

    # 3D Surface plot
    ax = plt.subplot(2, 3, (5, 6), projection='3d')
    X, Y = np.meshgrid(np.linspace(-3, 3, 50), np.linspace(-3, 3, 50))
    Z = np.sin(np.sqrt(X**2 + Y**2))
    ax.plot_surface(X, Y, Z, cmap='plasma')
    ax.set_title("3D Surface Plot")

    plt.tight_layout()
    plt.show()

visualize_data()
