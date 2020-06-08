# -*- coding: utf-8 -*-


class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        length = len(coordinates)
        if length < 2:
            return False
        coordinates = sorted(coordinates)
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        count = 1
        for i in range(1, length):
            if coordinates[i][0] == x0:
                count += 1
        if count == length:
            return True 
        count = 1
        for i in range(1, length):
            if coordinates[i][1] == y0:
                count += 1
        if count == length:
            return True 

        rowGrap = x1 - x0
        colGrap = y1 - y0

        for i in range(2, length):
            x0, y0 = coordinates[i-1]
            x1, y1 = coordinates[i]
            if (x1 - x0) / (y1 - y0) == rowGrap / colGrap:
                continue
            else:
                return False
        return True


if __name__ == "__main__":
    coordinates = [[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]]
    S = Solution()
    print(S.checkStraightLine(coordinates))