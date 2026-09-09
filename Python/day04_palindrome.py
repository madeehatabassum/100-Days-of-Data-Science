# Day 4: Palindrome Checker
# -------------------------
# Problem Statement:
# Given an integer x, return true if x is a palindrome, and false otherwise.

def is_palindrome(x):
    # Negative numbers and numbers ending with 0 (except 0 itself) are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
        
    reverted_half = 0
    while x > reverted_half:
        reverted_half = reverted_half * 10 + x % 10
        x //= 10
        
    # If the length is odd, we can get rid of the middle digit by reverted_half // 10
    return x == reverted_half or x == reverted_half // 10

if __name__ == "__main__":
    test_cases = [121, -121, 10, 1221]
    for num in test_cases:
        print(f"Is {num} a palindrome? {is_palindrome(num)}")
