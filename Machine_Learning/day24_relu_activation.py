# Day 24: ReLU Activation
# -----------------------
def relu(x):
    return max(0.0, x)
if __name__ == '__main__': print(relu(-5), relu(5))
