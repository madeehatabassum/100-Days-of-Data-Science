# Day 11: Valid Parentheses (Stack)
# ---------------------------------
# Problem Statement:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

def is_valid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
            
    return not stack

if __name__ == "__main__":
    test_strings = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for s in test_strings:
        print(f"'{s}' is valid: {is_valid(s)}")
