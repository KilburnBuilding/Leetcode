class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        charDict = dict()
        lengthSum = 0
        totalTimes = 0
        flag = False

        for i in s:
            if i not in charDict:
                charDict[i] = 0
            charDict[i] += 1
        
        for _, v in charDict.items():
            if v % 2 == 0:
                lengthSum += v
            else:
                lengthSum += v - 1
                totalTimes += 1
                flag = True
        
        if flag:
            totalLength = lengthSum + 1
        else: 
            totalLength = lengthSum 

        return totalLength


if __name__ == "__main__":
    t = "abccccdd"
    S = Solution()
    print(S.longestPalindrome(t))