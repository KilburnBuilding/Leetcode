# -*- coding: utf-8 -*-


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumValue = sum(nums)
        minValue = min(nums)
        lenValue = len(nums)
        minSetp = sumValue - lenValue * minValue

        return minSetp

    