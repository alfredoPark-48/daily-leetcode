# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 
import unittest

def product_except_self(nums):
    result = []
    prefix = 1
    postfix = 1

    for num in nums:
        result.append(prefix)
        prefix *= num
    
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
    
    return result

class TestProductExceptSelf(unittest.TestCase):
    def test_1(self):
        self.assertEqual(product_except_self([1,2,3,4]), [24,12,8,6], 'Should be [24,12,8,6]')
    
    def test_2(self):
        self.assertEqual(product_except_self([-1,1,0,-3,3]), [0,0,9,0,0], 'Should be [0,0,9,0,0]')

if __name__ == '__main__':
    unittest.main()