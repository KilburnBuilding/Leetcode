# -*- coding: utf-8 -*-


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1Length = len(num1)
        num2Length = len(num2)
        i = num1Length - 1
        j = num2Length - 1
        tempAdd = 0
        result = list()

        while i >= 0 or j >= 0:
            tempResult = 0
            if i >= 0 and j >= 0:
                tempResult = (ord(num1[i]) - ord('0')) + (ord(num2[j]) - ord('0')) + tempAdd
                i -= 1
                j -= 1
            elif i >= 0 and j < 0:
                tempResult = (ord(num1[i]) - ord('0')) + tempAdd
                i -= 1
            elif j >= 0 and i < 0:
                tempResult = (ord(num2[j]) - ord('0')) + tempAdd
                j -= 1
            tempAdd = 0
            if tempResult >= 10:
                tempAdd = 1
            tempChar = chr(tempResult % 10 + ord('0'))
            result.insert(0, tempChar)
        if tempAdd > 0:
            result.insert(0, '1')

        return ''.join(result)


if __name__ == "__main__":
    S = Solution()
    num1 = '1'
    num2 = '9'
    print(S.addStrings(num1, num2))