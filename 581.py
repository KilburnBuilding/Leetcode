# -*- coding: utf-8 -*-


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_index = -1
        right_index = -1
        total_number = 0

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                left_index = i -1
                break
        
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] <= nums[i - 1]:
                right_index = i
                break
        
        print('left_index', left_index)
        print('right_index', right_index)

        if left_index != -1 and right_index != -1:
            total_number = right_index - left_index + 1

        return total_number


if __name__ == "__main__":
    nums = [1,2,2,2, 3]
    S = Solution()
    print(S.findUnsortedSubarray(nums))