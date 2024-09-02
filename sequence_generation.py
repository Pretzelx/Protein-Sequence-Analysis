import random
import numpy as np

amino_acids = 'ACDEFGHIKLMNPQRSTVWY'

def generate_random_sequence(length, amino_acids=amino_acids):
    return ''.join(random.choice(amino_acids) for _ in range(length))

probabilities = np.array([0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
                          0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])

def generate_sequence(length):
    return ''.join(np.random.choice(list(amino_acids), size=length, p=probabilities))

# Example: Generate 10 random sequences of length 50
sequences = [generate_sequence(10) for _ in range(10)]

for i, seq in enumerate(sequences):
    print(f"Sequence {i+1}: {seq}")


