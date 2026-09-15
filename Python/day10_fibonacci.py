# Day 10: Fibonacci Sequence (Dynamic Programming)
# ------------------------------------------------
# Problem Statement:
# Write a function to return the nth number in the Fibonacci sequence.
# Optimize it using memoization (Dynamic Programming).

def fibonacci(n, memo={}):
    # Base cases
    if n == 0: return 0
    if n == 1: return 1
    
    # Check if already computed
    if n in memo:
        return memo[n]
        
    # Recursive step with memoization
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

if __name__ == "__main__":
    test_n = 50
    print(f"Fibonacci number {test_n} is: {fibonacci(test_n)}")
