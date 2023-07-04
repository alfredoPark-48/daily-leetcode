# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

import unittest

def contains_duplicate(nums):
  num_map = {}  
  for num in nums:
    if num in num_map:
      return True
    else:
      num_map[num] = num
  return False

class ContainsDuplicateTest(unittest.TestCase):
  def test_case1(self):
    self.assertEqual(contains_duplicate([1, 2, 3, 1]), True, 'Should be true')

  def test_case2(self):
    self.assertEqual(contains_duplicate([1, 2, 3, 4]), False, 'Should be false')

  def test_case3(self):
    self.assertEqual(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True, 'Should be true')

  def test_case4(self):
    self.assertEqual(contains_duplicate([]), False, 'Should be false')  # Empty list

  def test_case5(self):
    self.assertEqual(contains_duplicate([1]), False, 'Should be false')  # Single element

  def test_case6(self):
    self.assertEqual(contains_duplicate([1, 1]), True, 'Should be true')  # Duplicate elements

  def test_case7(self):
    self.assertEqual(contains_duplicate([1, 2, 3, 4, 5]), False, 'Should be false')  # No duplicates

  def test_case8(self):
    self.assertEqual(contains_duplicate([1, 2, 3, 4, 5, 1]), True, 'Should be true')  # Duplicate at the end

  def test_case9(self):
    self.assertEqual(contains_duplicate([1, 2, 3, 4, 5, 5]), True, 'Should be true')  # Duplicate in the middle

  def test_case10(self):
    self.assertEqual(contains_duplicate([1, 1, 2, 2, 3, 3, 4, 4]), True, 'Should be true')  # All elements are duplicates

if __name__ == '__main__':
    unittest.main()