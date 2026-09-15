# Day 9: Linear Regression Cost Function
# --------------------------------------
# Problem Statement:
# Write a function to compute the Mean Squared Error (MSE) cost for Linear Regression.

def compute_mse_cost(X, y, w, b):
    """
    Computes the Mean Squared Error cost.
    X: list of features
    y: list of target values
    w: weight
    b: bias
    """
    m = len(X)
    total_error = 0.0
    
    for i in range(m):
        prediction = (w * X[i]) + b
        error = prediction - y[i]
        total_error += (error ** 2)
        
    mse = (1.0 / (2 * m)) * total_error
    return mse

if __name__ == "__main__":
    X = [1.0, 2.0, 3.0]
    y = [1.5, 2.5, 3.5]
    w = 1.0
    b = 0.5
    cost = compute_mse_cost(X, y, w, b)
    print(f"The MSE cost is: {cost:.4f}")
