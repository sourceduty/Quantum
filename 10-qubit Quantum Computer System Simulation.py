# 10-qubit Quantum Computer System Simulation

import numpy as np

# Number of qubits
n_qubits = 10

# Initialize the state vector |000...0>
state_vector = np.zeros(2**n_qubits, dtype=complex)
state_vector[0] = 1.0  # The |000...0> state

# Function to apply Hadamard gate on a specific qubit
def apply_hadamard(state_vector, qubit, n_qubits):
    for i in range(2**n_qubits):
        if (i >> qubit) & 1 == 0:
            j = i | (1 << qubit)
            state_vector[i], state_vector[j] = (
                (state_vector[i] + state_vector[j]) / np.sqrt(2),
                (state_vector[i] - state_vector[j]) / np.sqrt(2),
            )

# Apply Hadamard gate to all qubits to create superposition
for qubit in range(n_qubits):
    apply_hadamard(state_vector, qubit, n_qubits)

# Function to apply a CNOT gate
def apply_cnot(state_vector, control_qubit, target_qubit, n_qubits):
    for i in range(2**n_qubits):
        if (i >> control_qubit) & 1 == 1:
            j = i ^ (1 << target_qubit)
            state_vector[i], state_vector[j] = state_vector[j], state_vector[i]

# Apply CNOT gate between qubits 0 and 1, and 2 and 3 to create entanglement
apply_cnot(state_vector, 0, 1, n_qubits)
apply_cnot(state_vector, 2, 3, n_qubits)

# Measure the probability distribution
probabilities = np.abs(state_vector) ** 2

# Get the outcome probabilities
outcome_probabilities = {format(i, f'0{n_qubits}b'): probabilities[i] for i in range(2**n_qubits)}

# Print the significant outcomes (non-zero probabilities)
significant_outcomes = {outcome: prob for outcome, prob in outcome_probabilities.items() if prob > 0.01}
significant_outcomes
