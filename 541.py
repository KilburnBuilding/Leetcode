# -*- coding: utf-8 -*-


class Solution(object):
    def __init__(self):
        self.s = ''

    def recursionWay(self, s, start, end, k):
        sLenght = len(s[start:end])

        if sLenght > 2 * k:
            self.recursionWay(s, start + 2 * k, end, k)
            tempList = s[start:start+k].copy()
            s[start:start+k] = tempList[::-1]

        if sLenght == 0:
            return

        if 0 < sLenght <= k:
            tempList = s[start:start+k].copy()
            s[start:start+k] = tempList[::-1]
            return

        if k < sLenght <= 2 * k:
            tempList = s[start:start+k].copy()
            s[start:start+k] = tempList[::-1]
            return 

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        self.s = list(s)
        self.recursionWay(self.s, 0, len(s), k)

        return ''.join(self.s)


if __name__ == "__main__":
    S = Solution()
    s = "abcdefg"
    k = 2
    print(S.reverseStr(s, k))
