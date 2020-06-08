# -*- coding: utf-8 -*-


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        childNum = len(g)
        g.sort()
        cookieNum = len(s)
        s.sort()
        i = 0
        j = 0
        result = 0

        while i < childNum and j < cookieNum:
            if g[i] <= s[j]:
                result += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return result


if __name__ == "__main__":
    A = [1, 2]
    B = [1, 2, 3]
    S = Solution()
    print(S.findContentChildren(A, B))