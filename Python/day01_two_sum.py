# Day 1: Two Sum Problem
# -----------------------
# Problem Statement:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def two_sum(nums, target):
    # Dictionary to store the numbers we have seen so far and their indices
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # If the complement exists in our dictionary, we found our pair!
        if complement in seen:
            return [seen[complement], i]
        
        # Otherwise, add the current number to the dictionary
        seen[num] = i
        
    return []

# Test the function
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(f"Indices: {two_sum(nums, target)}") # Expected: [0, 1]
