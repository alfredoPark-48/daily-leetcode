"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""

def is_valid(s):
    stack = []
    closing_brace = ['}', ')', ']']
    valid_braces = {
        '}':'{',
        ')':'(',
        ']':'['
    }

    for brace in s:
        if brace in closing_brace:
            if stack and stack[-1] == valid_braces[brace]:
                stack.pop()
            else:
                return False
        else:
            stack.append(brace)

    return True if not stack else False

print(is_valid('()'))
print(is_valid('()[]{}'))
print(is_valid('(]'))
