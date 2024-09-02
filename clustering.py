from sklearn.cluster import KMeans #KMeans is imported from sklearn.cluster, which is a machine learning algorithm used for clustering data.
import numpy as np

# Define the set of amino acids
amino_acids = 'ACDEFGHIKLMNPQRSTVWY'

def encode_sequence(sequence, amino_acids=amino_acids):
    return [amino_acids.index(aa) for aa in sequence]

def perform_clustering(sequences, n_clusters=2):
    encoded_sequences = np.array([encode_sequence(seq) for seq in sequences])
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(encoded_sequences)
    return kmeans.labels_
