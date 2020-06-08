# -*- coding: utf-8 -*-
import math


class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        remainder = 0
        result = list()
        for i in A:
            tempResult = remainder * 2 + i
            if tempResult % 5 == 0:
                result.append(True)
            else:
                result.append(False)
            remainder = tempResult % 5

        return result


if __name__ == "__main__":
    S = Solution()
    A = [0,1,1,1,1,1]
    print(S.prefixesDivBy5(A))