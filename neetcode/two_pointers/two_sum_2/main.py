# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

import unittest

def two_sum(numbers, target):
    pointer_one = 0
    pointer_two = len(numbers) - 1
    while pointer_one < pointer_two:
        if numbers[pointer_one] + numbers[pointer_two] == target:
            return [pointer_one + 1, pointer_two + 1]
        elif numbers[pointer_one] + numbers[pointer_two] > target:
            pointer_two -= 1
        else:
            pointer_one += 1
    return []

class TestTwoSum(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [1, 2], 'Should be [1, 2]')

    def test_case2(self):
        self.assertEqual(two_sum([2, 3, 4], 6), [1, 3], 'Should be [1, 3]')

    def test_case3(self):
        self.assertEqual(two_sum([-1, 0], -1), [1, 2], 'Should be [1, 2]')

if __name__ == '__main__':
    unittest.main()