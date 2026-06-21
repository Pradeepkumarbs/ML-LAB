# - Write a program to develop Principal Component Analysis (PCA)

from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

def pca_analysis():
    data = load_iris()
    X = data.data

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=data.target)
    plt.title("PCA Projection")
    plt.show()

pca_analysis()
