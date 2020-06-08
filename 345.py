# -*- coding: utf-8 -*-


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowelsSet = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        sCopy = list(s)
        record = list()
        for i in range(len(s)):
            if s[i] in vowelsSet:
                sCopy[i] = '-1'
                print(s[i])
                record.insert(0, s[i])
        for i in range(len(sCopy)):
            if sCopy[i] == '-1':
                sCopy[i] = record.pop(0)

        return ''.join(sCopy)


if __name__ == "__main__":
    s = "race car"
    S = Solution()
    print(S.reverseVowels(s))