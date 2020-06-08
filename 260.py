# -*- coding: utf-8 -*-


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        record = dict()
        result = list()

        for i in nums:
            if i not in record:
                record[i] = 0
            record[i] += 1
            
        for k, v in record.items():
            if v == 1:
                result.append(k)

        return result

