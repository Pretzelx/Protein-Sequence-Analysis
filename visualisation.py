import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np 
from clustering import encode_sequence


def plot_clusters(sequences, labels, reduced_data):
    plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=labels, cmap='viridis')
    for i, sequence in enumerate(sequences):
        plt.annotate(sequence, (reduced_data[i, 0], reduced_data[i, 1]))
    
    plt.title('PCA of Amino Acid Sequences')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.show()
