# -*- coding: utf-8 -*-


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        transfer = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        tempResult = list()
        tempValue = 0
        if num < 0:
            num = 256 * 256 * 256 * 256 + num
        if num < 10:
            return str(num)
        elif num < 16:
            return transfer[num]
        else:
            while num >= 16:
                tempValue = num % 16
                if tempValue >= 10:
                    tempResult.insert(0, transfer[tempValue])
                else:
                    tempResult.insert(0, str(tempValue))
                num = int(num / 16)
            if num >= 10:
                tempResult.insert(0, transfer[num])
            else:
                tempResult.insert(0, str(num))

        return ''.join(tempResult)


if __name__ == "__main__":
    Input = -1
    S = Solution()
    print(S.toHex(Input))