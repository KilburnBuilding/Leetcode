# -*- coding: utf-8 -*-


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        else:
            charTotal = self.countAndSay(n - 1)
            charStart = charTotal[0]
            charCount = 0
            tempResult = list()
            for i in range(len(charTotal)):
                if charTotal[i] == charStart:
                    charCount += 1
                else:
                    tempResult.append(str(charCount))
                    tempResult.append(str(charStart))
                    charCount = 1
                    charStart = charTotal[i]
            tempResult.append(str(charCount))
            tempResult.append(str(charStart))

            return ''.join(tempResult)


if __name__ == "__main__":
    n = 4
    S = Solution()
    print(S.countAndSay(n))
