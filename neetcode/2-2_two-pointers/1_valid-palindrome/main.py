# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the
# same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not is_alpha_numeric(s[left].lower()):
            left += 1
        while right > left and not is_alpha_numeric(s[right].lower()):
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left, right = left + 1, right - 1
    return True


def is_alpha_numeric(char):
    return ord("a") <= ord(char) <= ord("z") or ord("0") <= ord(char) <= ord("9")

    
print(is_palindrome('A man, a plan, a canal: Panama'))
print(is_palindrome('race a car'))
print(is_palindrome(' '))
