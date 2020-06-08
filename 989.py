# -*- coding: utf-8 -*-


class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        A = [str(i) for i in A]
        intA = int(''.join(A))
        sumAK = intA + K
        strAK = str(sumAK)

        result = [int(i) for i in strAK]
        
        return result


if __name__ == "__main__":
    A = [1,2,0,0]
    K = 34
    S = Solution()
    print(S.addToArrayForm(A, K))