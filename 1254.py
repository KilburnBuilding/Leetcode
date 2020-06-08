# -*- coding: utf-8 -*-


class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 
        
        rows = len(grid)
        cols = len(grid[0])
        