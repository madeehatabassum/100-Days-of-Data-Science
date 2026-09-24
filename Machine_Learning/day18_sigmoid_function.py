# Day 18: Sigmoid Function (Logistic Regression)
# ----------------------------------------------
# Problem Statement:
# Write a function to implement the sigmoid activation function used in Logistic Regression.
# Formula: S(x) = 1 / (1 + e^-x)

import math

def sigmoid(x):
    """
    Computes the sigmoid of x.
    """
    return 1 / (1 + math.exp(-x))

if __name__ == "__main__":
    test_values = [-10, -1, 0, 1, 10]
    for val in test_values:
        print(f"Sigmoid({val:3}) = {sigmoid(val):.4f}")
