# -*- coding: utf-8 -*-


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        tempResult = dict()
        reflectResult = dict()
        maxValue = float('-inf')
        result = ""

        for i in s:
            tempResult[i] = tempResult.get(i, 0) + 1
        
        for k, v in tempResult.items():
            if v > maxValue:
                maxValue = v
            if v not in reflectResult:
                reflectResult[v] = list()
            reflectResult[v].append(k)

        for i in range(maxValue, -1, -1):
            temp = reflectResult.get(i, list())
            if temp:
                for j in temp:
                    result += i * j

        return result


if __name__ == "__main__":
    s = 'tree'
    S = Solution()
    print(S.frequencySort(s))