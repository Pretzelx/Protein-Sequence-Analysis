import numpy as np
from sequence_generation import generate_random_sequence
from clustering import perform_clustering
from visualisation import plot_clusters

def main():
    num_sequences = 40
    sequence_length = 10

    sequences = [generate_random_sequence(sequence_length) for _ in range(num_sequences)]
    labels, reduced_data = perform_clustering(sequences, n_clusters=3)
    
    plot_clusters(sequences, labels, reduced_data)

if __name__ == "__main__":
    main()
