# -*- coding: utf-8 -*-


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        tempDict1 = dict()
        tempDict2 = dict()
        tempSet1 = set(list1)
        tempSet2 = set(list2)
        result = list()
        resultDict = dict()

        totalSet = tempSet1 & tempSet2 
        for index, res in enumerate(list1):
            tempDict1[res] = index
        
        for index, res in enumerate(list2):
            tempDict2[res] = index

        minSum = float('inf')
        tempResult = ''
        if len(totalSet) == 1:
            tempResult = totalSet.pop()
            result.append(tempResult)
        else:
            for i in totalSet:
                tempSum = tempDict1[i] + tempDict2[i]
                if minSum >= tempSum:
                    minSum = tempSum
                if tempSum not in resultDict:
                    resultDict[tempSum] = list()
                resultDict[tempSum].append(i)

            result.extend(resultDict[minSum])

        return result


if __name__ == "__main__":
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["KFC","Shogun","Burger King"]
    S = Solution()
    print(S.findRestaurant(list1, list2))
    