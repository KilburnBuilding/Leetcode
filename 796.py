# -*- coding: utf-8 -*-


class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        for i in range(len(A)):
            if A[i:] + A[:i] == B:
                return True
        return False


if __name__ == "__main__":
    A = 'abcde'
    B = 'cdeab'
    S = Solution()
    print(S.rotateString(A, B))