"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1


Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

"""


def singleNumber(nums): 
  ret = 0
  for i in nums:
     ret ^= i    
  return ret

n=singleNumber([1,1,5,3,3,4,4])       
print("Ans:",n)     # Ans: 5   