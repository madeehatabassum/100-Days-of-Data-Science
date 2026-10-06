# Day 30: Mean Absolute Error
# ---------------------------
def mae(y_true, y_pred):
    return sum(abs(yt - yp) for yt, yp in zip(y_true, y_pred)) / len(y_true)
if __name__ == '__main__': print(mae([3, -0.5, 2, 7], [2.5, 0.0, 2, 8]))
