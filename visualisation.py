import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np 
from clustering import encode_sequence

# Define the set of amino acids
amino_acids = 'ACDEFGHIKLMNPQRSTVWY'

def plot_clusters(sequences, labels, amino_acids=amino_acids):
    encoded_sequences = np.array([encode_sequence(seq) for seq in sequences])
    pca = PCA(n_components=2)
    reduced_data = pca.fit_transform(encoded_sequences)
    plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=labels)
    plt.title('Clustering of Amino Acid Sequences')
    plt.show()