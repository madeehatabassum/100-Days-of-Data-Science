# Day 40: Move Zeroes in Place
# -----------------------------
# Problem Statement:
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements in-place.

def move_zeroes(nums):
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1

if __name__ == '__main__':
    arr = [0, 1, 0, 3, 12]
    move_zeroes(arr)
    print(f'Result: {arr}')
