/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
*/

const twoSum = (numList: Array<number>, target: number) => {
	let numObject: object = {}
  for (let i=0; i<numList.length; i++) {
    if (numObject.hasOwnProperty(numList[i])) {
      if (numObject[numList[i]][1] + numList[i] === target) {
        return [i, numObject[numList[i]][0]]
      }
    } else {
      if (target <= numList[i]) {
        numObject[numList[i] - target] = [i, numList[i]-(numList[i]-target)]
      } else {
        numObject[target-numList[i]] = [i, target - (target-numList[i])]
      }
    }
  }
	
  return [-1,-1]
}
export default twoSum
console.log(twoSum([2,7,11,15], 9))
console.log(twoSum([3,2,4], 6))
