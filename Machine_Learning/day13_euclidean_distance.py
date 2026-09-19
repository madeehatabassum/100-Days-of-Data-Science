# Day 13: Euclidean Distance (Foundation of K-Means)
# --------------------------------------------------
# Problem Statement:
# Write a function to calculate the Euclidean distance between two n-dimensional points.

import math

def euclidean_distance(point1, point2):
    """
    Calculates the Euclidean distance between two points.
    point1 and point2 should be lists or tuples of the same length.
    """
    if len(point1) != len(point2):
        raise ValueError("Points must have the same number of dimensions.")
        
    squared_distance = sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2))
    return math.sqrt(squared_distance)

if __name__ == "__main__":
    p1 = [1, 2, 3]
    p2 = [4, 5, 6]
    
    dist = euclidean_distance(p1, p2)
    print(f"The Euclidean distance between {p1} and {p2} is: {dist:.4f}")
