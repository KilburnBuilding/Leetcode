# -*- coding: utf-8 -*-


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rowLength = len(grid)
        colLength = len(grid[0])
        queueRecordOne = list()
        second = 0
        for i in range(rowLength):
            for j in range(colLength):
                if grid[i][j] == 2:
                    if i < rowLength -1 and grid[i+1][j] == 1 and [i+1, j] not in queueRecordOne:
                        queueRecordOne.append([i+1,j])
                    if i > 0 and grid[i-1][j] == 1 and [i-1, j] not in queueRecordOne:
                        queueRecordOne.append([i-1, j])
                    if j < colLength -1 and grid[i][j + 1] == 1 and [i, j+1] not in queueRecordOne:
                        queueRecordOne.append([i, j+1])
                    if j > 0 and grid[i][j -1 ] == 1 and [i, j-1] not in queueRecordOne:
                        queueRecordOne.append([i, j - 1])

        if queueRecordOne:
            second += 1
        queueRecordTwo = list()

        while queueRecordOne:
            print('queueRecordOne: ',queueRecordOne)
            rowRocord, colRecord = queueRecordOne.pop(0)
            grid[rowRocord][colRecord] = 2
            if rowRocord < rowLength -1 and grid[rowRocord + 1][colRecord] == 1 and [rowRocord +1, colRecord] not in queueRecordTwo and [rowRocord +1, colRecord] not in queueRecordOne:
                queueRecordTwo.append([rowRocord + 1, colRecord])
            if rowRocord > 0 and grid[rowRocord - 1][colRecord] == 1 and [rowRocord - 1, colRecord] not in queueRecordTwo and [rowRocord - 1, colRecord] not in queueRecordOne:
                queueRecordTwo.append([rowRocord -1, colRecord])
            if colRecord < colLength - 1 and grid[rowRocord][colRecord + 1] == 1 and [rowRocord, colRecord + 1] not in queueRecordTwo and [rowRocord, colRecord + 1] not in queueRecordOne:
                queueRecordTwo.append([rowRocord, colRecord + 1])
            if colRecord > 0 and grid[rowRocord][colRecord - 1] == 1 and [rowRocord, colRecord -1] not in queueRecordTwo and [rowRocord, colRecord -1] not in queueRecordOne:
                queueRecordTwo.append([rowRocord, colRecord - 1])

            print('queueRecordTwo: ', queueRecordTwo)
            if not queueRecordOne and queueRecordTwo:
                second +=1
                queueRecordOne = queueRecordTwo[:]
                queueRecordTwo = list()
            
            print('sceond: ', second)

        for i in range(rowLength):
            for j in range(colLength):
                if grid[i][j] == 1:
                    second = -1
        
        return second
                    

if __name__ == "__main__":
    a = [[2,1,1],[1,1,0],[0,1,1]]
    S = Solution()
    print(S.orangesRotting(a))