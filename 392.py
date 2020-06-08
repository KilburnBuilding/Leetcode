# -*- coding: utf-8 -*-


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sLength = len(s)
        tLength = len(t)
        i = 0
        j = 0
        while i < sLength and j < tLength:
            if s[i] == t[j]:
                i = i + 1
                j = j + 1
            else:
                j = j + 1
            
        if i < sLength:
            return False
        else:
            return True


if __name__ == "__main__":
    s = "axc"
    t = "ahbgdc"
    S = Solution()
    print(S.isSubsequence(s, t))
            
         