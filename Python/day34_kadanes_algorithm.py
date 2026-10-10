# Day 34: Maximum Subarray (Kadane\'s Algorithm)
# --------------------------------------------
def max_sub_array(nums):
    current_sum = max_sum = nums[0]
    for x in nums[1:]:
        current_sum = max(x, current_sum + x)
        max_sum = max(max_sum, current_sum)
    return max_sum

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f'Max Subarray Sum: {max_sub_array(nums)}')
