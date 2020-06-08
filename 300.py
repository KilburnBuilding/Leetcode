# -*- coding: utf-8 -*-


class Solution(object):
    def remove(self):
        
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = 0
        length = len(nums)
        result = [0 for _ in range(length)]

        for i in range(length):
            temp_value = 1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    temp_value = max(temp_value, result[j] + 1)
            result[i] = temp_value
            if result[i] > max_value:
                max_value = result[i]

        return max_value


if __name__ == "__main__":
    s = Solution()
    nums = [10,9,2,5,3,7,101,18]
    print(s.lengthOfLIS(nums))