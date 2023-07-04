# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

import unittest


def two_sum(nums, target):
    num_map = {}
    for index, num in enumerate(nums):
        difference = target - num
        if difference in num_map:
            return [num_map[difference], index]
        num_map[num] = index
    return []


class TwoSumTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1], "Should be [0,1]")

    def test_case2(self):
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2], "Should be [1,2]")

    def test_case3(self):
        self.assertEqual(two_sum([3, 3], 6), [0, 1], "Should be [0,1]")

    def test_case4(self):
        self.assertEqual(two_sum([1, 2, 3, 4, 5], 7), [2, 3], "Should be [2, 3]")

    def test_case5(self):
        self.assertEqual(two_sum([-1, 0, 1, 2, -2], 0), [0, 2], "Should be [0, 2]")

    def test_case6(self):
        self.assertEqual(two_sum([9, 8, 7, 6, 5], 14), [1, 3], 'Should be [1, 3]')

    def test_case7(self):
        self.assertEqual(two_sum([4, 3, 2, 1], 5), [1, 2], 'Should be [0, 3]')

    def test_case8(self):
        self.assertEqual(two_sum([-3, -2, -1, 0, 1, 2, 3], 0), [2, 4], 'Should be [2, 4]')

    def test_case9(self):
        self.assertEqual(two_sum([7, 7, 7, 7, 7], 14), [0, 1], 'Should be [0, 1]')

    def test_case10(self):
        self.assertEqual(two_sum([10, 20, 30, 40], 100), [], 'Should be []')

if __name__ == "__main__":
    unittest.main()
