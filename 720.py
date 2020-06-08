# -*- coding: utf-8 -*-


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        wset = set([''])
        ans = ''
        for word in sorted(words):
            if word[:-1] in wset:
                wset.add(word)
                print('word[:-1]', word[:-1])
                if len(word) > len(ans):
                    ans = word
        return ans


if __name__ == "__main__":
    words = ["w", "wo", "wor", "worl", "world"]
    S = Solution()
    print(S.longestWord(words))