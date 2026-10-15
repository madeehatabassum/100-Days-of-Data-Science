# Day 39: K-Nearest Neighbors (KNN) from Scratch
# ---------------------------------------------
import math
from collections import Counter

def euclidean_dist(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def knn_predict(X_train, y_train, x_test, k=3):
    distances = [(euclidean_dist(x_test, x), label) for x, label in zip(X_train, y_train)]
    distances.sort(key=lambda item: item[0])
    k_nearest_labels = [label for _, label in distances[:k]]
    most_common = Counter(k_nearest_labels).most_common(1)
    return most_common[0][0]

if __name__ == '__main__':
    X_train = [[1, 2], [2, 3], [3, 1], [6, 5], [7, 7], [8, 6]]
    y_train = [0, 0, 0, 1, 1, 1]
    sample = [2, 2]
    pred = knn_predict(X_train, y_train, sample, k=3)
    print(f'Prediction for {sample}: Class {pred}')
