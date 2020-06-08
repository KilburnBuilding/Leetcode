# -*- -*-


class Solution(object):
    def __init__(self):
        self.maxArea = 0

    def landArea(self, grid, record, i, j, colLength, rowLength):
        if i < 0 or i >= rowLength or j < 0 or j >= colLength:
            return 
        if record[i][j] == 1:
            return 
        if grid[i][j] != 1:
            return
        if grid[i][j] == 1:
            self.maxArea += 1
            record[i][j] = 1
        self.landArea(grid, record, i + 1, j, colLength, rowLength)
        self.landArea(grid, record, i - 1, j, colLength, rowLength)
        self.landArea(grid, record, i, j - 1, colLength, rowLength)
        self.landArea(grid, record, i, j + 1, colLength, rowLength)


    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 
        colLength = len(grid[0])
        rowLength = len(grid)
        record = [[0 for i in range(colLength)] for _ in range(rowLength)]
        maxArea = 0

        for i in range(rowLength):
            for j in range(colLength):
                if grid[i][j] == 1:
                    self.maxArea = 0
                    self.landArea(grid, record, i, j, colLength, rowLength)
                    if maxArea < self.maxArea:
                        maxArea = self.maxArea
        
        return maxArea


if __name__ == "__main__":
    # a = [[0,0,1,0,0,0,0,1,0,0,0,0,0], [0,0,0,0,0,0,0,1,1,1,0,0,0], [0,1,1,0,1,0,0,0,0,0,0,0,0], [0,1,0,0,1,1,0,0,1,0,1,0,0], [0,1,0,0,1,1,0,0,1,1,1,0,0], [0,0,0,0,0,0,0,0,0,0,1,0,0], [0,0,0,0,0,0,0,1,1,1,0,0,0], [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    a = [[0,0,0,0,0,0,0,0]]
    S = Solution()
    print(S.maxAreaOfIsland(a))