import math

import numpy as np

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])

######################### Intermediate
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

######################### Advanced
# def sigmoid(z):
#     return sum(z)

# calculate the output of the sigmoid for x with all three coefficients
z1 = np.dot(c1, x)
z2 = np.dot(c2, x)
z3 = np.dot(c3, x)

output1 = sigmoid(z1)
output2 = sigmoid(z2)
output3 = sigmoid(z3)

print(f"Coefficient set 1: z = {z1:.4f}, sigmoid(z) = {output1:.4f}")
print(f"Coefficient set 2: z = {z2:.4f}, sigmoid(z) = {output2:.4f}")
print(f"Coefficient set 3: z = {z3:.4f}, sigmoid(z) = {output3:.4f}")


# Find which coefficient set yields the highest output
max_output = max(output1, output2, output3)
if max_output == output1:
    print("\nCoefficient set 1 yields the highest sigmoid output")
elif max_output == output2:
    print("\nCoefficient set 2 yields the highest sigmoid output")
else:
    print("\nCoefficient set 3 yields the highest sigmoid output")