# -*- coding: utf-8 -*-


class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1, y1, x2, y2 = rec1
        m1, n1, m2, n2 = rec2
        if min([x2, m2]) > max([x1, m1]) and min([y2, n2]) > max([y1, n1]):
            return True
        return False


        

if __name__ == "__main__":
    