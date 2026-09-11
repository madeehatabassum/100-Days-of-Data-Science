# Day 6: Gradient Descent Basics
# ------------------------------
# Problem Statement:
# Implement a simple Gradient Descent algorithm to find the local minimum of a function.
# Function: f(x) = x^2 (The derivative is f'(x) = 2x)

def gradient_descent(starting_x, learning_rate, num_iterations):
    x = starting_x
    for i in range(num_iterations):
        # Calculate the gradient (derivative of x^2)
        gradient = 2 * x
        
        # Take a step in the opposite direction of the gradient
        x = x - (learning_rate * gradient)
        
        if (i+1) % 5 == 0:
            print(f"Iteration {i+1}: x = {x:.4f}, f(x) = {x**2:.4f}")
            
    return x

if __name__ == "__main__":
    print("Starting Gradient Descent...")
    final_x = gradient_descent(starting_x=10, learning_rate=0.1, num_iterations=30)
    print(f"Local minimum occurs at x = {final_x:.4f}")
