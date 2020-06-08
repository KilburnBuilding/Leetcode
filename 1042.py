# -*- coding: utf-8 -*-


class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        result = [0 for i in range(N)]
        graphList = [list() for i in range(N)]
        for i in paths:
            graphList[i[0] -1].append(i[1] - 1)
            graphList[i[1] -1].append(i[0] - 1)

        for i in range(N):
            neighTop = list()
            for j in graphList[i]:
                neighTop.append(result[j])
            for n in range(1, 5):
                if n not in neighTop:
                    result[i] = n

        return result

if __name__ == "__main__":
    N = 4
    paths = [[1,2],[3,4]]
    S = Solution()
    print(S.gardenNoAdj(N, paths))

            
