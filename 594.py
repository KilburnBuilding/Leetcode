# -*- coding: utf-8 -*-


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tempDict = dict()
        for i in nums:
            if i not in tempDict:
                tempDict[i] = 0
            tempDict[i] += 1
        
        maxLength = 0
        maxList = list()
        for k, v in tempDict.items():
            tempLength = v + tempDict.get(k + 1, 0)
            if tempLength > maxLength and tempDict.get(k + 1, 0) != 0:
                maxLength = tempLength
                maxList = list()
                maxList.append([k, k + 1])

            tempLength = v + tempDict.get(k - 1, 0)
            if tempLength > maxLength and tempDict.get(k - 1, 0) != 0:
                maxLength = tempLength
                maxList = list()
                maxList.append([k - 1, k])

        return maxLength


if __name__ == "__main__":
    nums = [1, 1, 1, 1]
    S = Solution()
    print(S.findLHS(nums))
 


                

        


