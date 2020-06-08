# -*- coding: utf-8 -*-

"""
    超时了，但是解法应该是没有问题的
"""
# class Solution(object):
#     def compare(self, word1, word2):
#         if not word1 and not word2:
#             return 0

#         if word1 and not word2:
#             return len(word1)
        
#         if not word1 and word2:
#             return len(word2)

#         if word1[-1] == word2[-1]:
#             return min(self.compare(word1[:-1], word2[:-1]), self.compare(word1[:-1], word2), self.compare(word1, word2[:-1]))
        
#         if word1[-1] != word2[-1]:
#             return 1 + min(self.compare(word1[:-1], word2[:-1]), self.compare(word1[:-1], word2), self.compare(word1, word2[:-1]))

#     def minDistance(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: int
#         """
#         return self.compare(word1, word2)


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        length1 = len(word1)
        length2 = len(word2)

        result = [[ 0 for _ in range(length1+ 1)] for _ in range(length2 + 1)]

        for i in range(length2+1):
            result[i][0] = i
        
        for j in range(length1+1):
            result[0][j] = j
        
        for index2 in range(1, length2 + 1):
            for index1 in range(1, length1 + 1):
                if word1[index1 - 1] != word2[index2 - 1]:
                    result[index2][index1] = 1 + min(result[index2 - 1][index1 - 1], result[index2 - 1][index1], result[index2][index1 - 1])
                else:
                    result[index2][index1] = min(result[index2 - 1][index1 - 1], result[index2 - 1][index1], result[index2][index1-1])
        return result[-1][-1]


if __name__ == "__main__":
    word1 = ""
    word2 = "a"
    S = Solution()
    print(S.minDistance(word1, word2))
