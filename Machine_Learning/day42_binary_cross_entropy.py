# Day 42: Binary Cross Entropy (Log Loss) from Scratch
# ----------------------------------------------------
import math

def binary_cross_entropy(y_true, y_pred, eps=1e-15):
    # Clip predictions to prevent log(0)
    total_loss = 0.0
    n = len(y_true)
    for y, p in zip(y_true, y_pred):
        p_clipped = max(eps, min(1 - eps, p))
        total_loss += -(y * math.log(p_clipped) + (1 - y) * math.log(1 - p_clipped))
    return total_loss / n

if __name__ == '__main__':
    y_true = [1, 0, 1, 1]
    y_pred = [0.9, 0.1, 0.8, 0.4]
    print(f'Log Loss: {binary_cross_entropy(y_true, y_pred):.4f}')
