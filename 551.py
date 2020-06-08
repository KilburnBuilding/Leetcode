# -*- coding: utf-8 -*-


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tempL = 0
        tempA = 0
        for i in s:
            if i == 'L':
                tempL += 1
            else:
                tempL = 0
                if i == 'A':
                    tempA += 1
            if tempL > 2:
                return False
            if tempA > 1:
                return False

        return True


if __name__ == "__main__":
    A = "PPALLL"
    S = Solution()
    print(S.checkRecord(A))