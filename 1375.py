# -*- coding: utf-8 -*-


class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        maxValue = float('-inf')
        tempRecord = list()
        result = 0
        for i in light:
            if i > maxValue:
                maxValue = i
            tempRecord.append(i)
            if maxValue == len(tempRecord):
                result += 1
        
        return result
                            

if __name__ == "__main__":
    light = [1,2,3,4,5,6]
    S = Solution()
    print(S.numTimesAllBlue(light))


