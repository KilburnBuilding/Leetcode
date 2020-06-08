# -*- coding: utf-8 -*-


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        tempDict = dict()
        for c in "!?',;.":
            paragraph = paragraph.replace(c, ' ')

        for i in paragraph.split(' '):
            i = i.strip('.').strip(',').strip('!').strip('?')
            if not i:
                continue
            if i.lower() not in tempDict:
                tempDict[i.lower()] = 0
            tempDict[i.lower()] += 1
        sortedDict = sorted(tempDict.items(), key=lambda x: x[1], reverse=True)

        for k, v in sortedDict:
            if k not in banned:
                return k
            

if __name__ == "__main__":
    paragraph = "a, a, a, a, b,b,b,c, c"
    banned = ["a"]
    S = Solution()
    print(S.mostCommonWord(paragraph, banned))