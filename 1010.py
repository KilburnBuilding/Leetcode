# -*- coding: utf-8 -*-


class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        result = 0
        recordDict = dict()
        for i in time:
            if i % 60 != 0:
                result += recordDict.get(60 - i % 60, 0)
            else:
                result += recordDict.get(0, 0)
            if i % 60 not in recordDict:
                recordDict[i % 60] = 0
            recordDict[i % 60] += 1
        
        return result


if __name__ == "__main__":
    timeList = [60, 60, 60]
    S = Solution()
    print(S.numPairsDivisibleBy60(timeList))