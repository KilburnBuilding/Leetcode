# -*- coding: utf-8 -*-


class Solution(object):
    def __init__(self):
        self._record = list()
        self._text_1 = ''
        self._text_2 = '' 
        self._length_1 = 0
        self._length_2 = 0
        self._record = list()

    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        self._text_1 = text1
        self._text_2 = text2
        self._length_1 = len(text1)
        self._length_2 = len(text2)
        index_1 = 0
        index_2 = 0
        self._record = [[0 for i in range(self._length_2 + 1)] for _ in range(self._length_1 + 1)]
        for index_1 in range(self._length_1):
            for index_2 in range(self._length_2):
                if text1[index_1] == text2[index_2]:
                    self._record[index_1 + 1][index_2 + 1] = self._record[index_1][index_2] + 1
                else:
                    self._record[index_1 + 1][index_2 + 1] = max(self._record[index_1 + 1][index_2], self._record[index_1][index_2 + 1])

        return result[-1][-1]


if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"
    S = Solution()
    print(S.longestCommonSubsequence(text1, text2))