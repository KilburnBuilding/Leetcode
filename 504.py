# -*- coding: utf-8 -*-


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        symbol = ''
        result = ''

        if num < 0:
            symbol = '-'
            num = num * (-1)

        if num == 0:
            return '0'
            
        while num > 0:
            result = str(num % 7) + result
            num = num // 7

        result = symbol + result
    
        return result


if __name__ == "__main__":
    num = 0
    S = Solution()
    print(S.convertToBase7(num))
        