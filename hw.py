import numpy as np

# Example data
x = np.array([0.1, 0.2, 0.3])  # Your input data
W = np.array([[0.5, 0.6, 0.7],  # Weight matrix
              [0.8, 0.9, 1.0],
              [1.0, 1.2, 1.3]])
b = np.array([1.5, 1.6, 1.7])  # Bias

# Reshape x
x = x.reshape(1, 3)

# Matrix multiplication
result = np.dot(x, W) + b 
print(result)

#Question2 

import numpy as np

# Weights
w = np.array([[0.5, 0.6, 0.7],
              [0.8, 0.9, 1.0],
              [1.0, 1.2, 1.3]])

# Biases
b = np.array([0.5, 0.6, -1.7])

# Input vector
x = np.array([0.1, 0.2, 0])

# Dot product of weight matrix and input vector
z = np.dot(x, w)

# Add biases
z = z + b

# Output
print(z)