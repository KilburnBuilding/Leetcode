# -*- coding: utf-8 -*-


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        record = [[0 for i in range(length)] for j in range(length)]
        for i in range(length):
            record[i][i] = 1
        
        for j in range(1, length):
            for i in range(j):
                if j - i + 1 == 2:
                    if s[j] == s[j-1]:
                        record[i][j] = 1
                if j - i + 1 > 2:
                    if s[i] == s[j] and record[i+1][j -1] == 1:
                        record[i][j] = 1
        result = 0
        for i in range(length):
            for j in range(i, length):
                if record[i][j] == 1:   
                    result += 1
        for i in record:
            print(i)
        
        return result
                 

if __name__ == "__main__":
    S = Solution()
    s = "aba"
    print(S.countSubstrings(s))