# Day 21: K-Means Clustering Core Logic
# -------------------------------------
# Problem Statement:
# Implement the centroid assignment step for K-Means Clustering.

import math

def euclidean_distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def assign_clusters(data, centroids):
    """
    Assigns each data point to the nearest centroid.
    """
    clusters = []
    for point in data:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        closest_index = distances.index(min(distances))
        clusters.append(closest_index)
    return clusters

if __name__ == "__main__":
    data_points = [(1, 2), (2, 1), (8, 9), (9, 8)]
    centroids = [(0, 0), (10, 10)]
    
    assignments = assign_clusters(data_points, centroids)
    print("Point Assignments (Index of Centroid):", assignments)
