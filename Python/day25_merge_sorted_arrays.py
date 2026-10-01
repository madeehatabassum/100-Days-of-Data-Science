# Day 25: Merge Sorted Arrays
# ---------------------------
def merge(nums1, m, nums2, n):
    nums1[m:] = nums2
    nums1.sort()
if __name__ == '__main__': 
    n1 = [1,2,3,0,0,0]; merge(n1, 3, [2,5,6], 3); print(n1)
