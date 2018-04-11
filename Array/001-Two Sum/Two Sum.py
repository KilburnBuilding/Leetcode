"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
"""
"""
思路：
    1. 利用哈希表，用空间换时间
    2. 改变一下思路，key值为给定的值，value值为该值顺序索引
    3. 字典的key值不能重复，所以遍历list，而不是遍历构造好的字典 
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        test = dict()
        for i in range(len(nums)):
            test[nums[i]] = i

        for i in range(len(nums)):
            gap = target - nums[i]
            try:
                if test[gap] and test[gap] > i:
                    return [i, test[gap]]
            except Exception as e:
                pass
