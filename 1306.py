# -*- coding: utf-8 -*-


class Solution(object):
    def solve(self, arr, start, targetIndex, length, record):
        if start >= length or record[start]:
            return False
        if start < 0 or record[start]:
            return False
        if start == targetIndex:
            return True
        record[start] = 1
        return self.solve(arr, start - arr[start], targetIndex, length, record) or self.solve(arr, start + arr[start], targetIndex, length, record)

    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        if not arr:
            return False
        length = len(arr)
        targetList = list()

        for i in range(length):
            if arr[i] == 0:
                targetList.append(i)

        for targetIndex in targetList:
            record = [0 for i in range(length)]
            result = self.solve(arr, start, targetIndex, length, record)
        
            if result:
                return True
        return False


if __name__ == "__main__":
    arr = [0,3,0,6,3,3,4]
    start = 6
    # arr = [3,0,2,1,2]
    # start = 2
    S = Solution()
    print(S.canReach(arr, start))