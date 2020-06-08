# -*- coding: utf-8 -*-


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = set()
        sumTemp = 0

        while n != 1:
            sumTemp = 0
            while n:
                sumTemp += (n % 10) * (n % 10)
                n = n // 10
            
            n = sumTemp
            if sumTemp not in result:
                result.add(sumTemp)
            else:
                break
        
        return n == 1


if __name__ == "__main__":
    S = Solution()
    print(S.isHappy(19))