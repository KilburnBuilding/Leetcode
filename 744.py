# -*- coding: utf-8 -*-


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        result = ''
        if target >= letters[-1]:
            result = letters[0]
        else:
            for i in letters:
                if target >= i:
                    continue
                else:
                    result = i
                    break
        
        return result


if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = "k"
    S = Solution()
    print(S.nextGreatestLetter(letters, target))