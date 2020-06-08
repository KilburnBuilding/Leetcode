# -*- coding: utf-8 -*-
import copy


class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        result = 0
        tempDict = dict()

        for i in dominoes:
            m, n = i[0], i[1]
            if m < n:
                m, n = n, m
            tempKey = '%s_%s' % (m, n)
            if tempKey not in tempDict:
                tempDict[tempKey] = 1
            else:
                result += tempDict[tempKey]
                tempDict[tempKey] += 1
        
        return result


if __name__ == "__main__":
    dominoes = [[1,2],[2,1],[3,4],[5,6]]
    S = Solution()
    print(S.numEquivDominoPairs(dominoes))