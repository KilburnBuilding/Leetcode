# -*- coding: utf-8 -*-


class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        result = set()
        tempRecord = [[0 for _ in range(N)] for _ in range(N)]
        for i in trust:
            tempRecord[i[0]-1][i[1]-1] = 1
        for i in range(N):
            if sum(tempRecord[i]) == 0:
                tempSum = 0
                for j in range(N):
                    tempSum += tempRecord[j][i]
                if tempSum == N - 1:
                    result.add(i + 1)

        if len(result) != 1:
            return -1
        else:
            return result.pop()


if __name__ == "__main__":
    S = Solution()
    N = 3
    trust = [[1,3],[2,3],[3,1]]
    print(S.findJudge(N, trust))