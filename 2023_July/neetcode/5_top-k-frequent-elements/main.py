# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

def top_k_frequent(nums, k):
    num_map = {}
    frequent_nums = [[] for i in range(len(nums) + 1)]
    for num in nums:
        if num in num_map:
            num_map[num] += 1
        else:
            num_map[num] = 1

    for num, count in num_map.items():
        frequent_nums[count].append(num)
    
    result = []
    for i in range(len(frequent_nums) - 1, 0, - 1):
        for num in frequent_nums[i]:
            result.append(num)
            if len(result) == k:
                print(result)
                return result


top_k_frequent([1,1,1,2,2,3], 2)
top_k_frequent([1], 1)