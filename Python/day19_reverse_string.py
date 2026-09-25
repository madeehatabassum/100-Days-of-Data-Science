# Day 19: Reverse String in Place
# -------------------------------
# Problem Statement:
# Write a function that reverses a string (represented as an array of characters).
# Do not allocate extra space; do it in-place with O(1) extra memory.

def reverse_string(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

if __name__ == "__main__":
    char_array = ["h", "e", "l", "l", "o"]
    print(f"Original: {char_array}")
    reverse_string(char_array)
    print(f"Reversed: {char_array}")
