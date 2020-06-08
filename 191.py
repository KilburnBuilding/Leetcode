# -*- coding: utf-8 -*-


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += n&1
            n >>= 1
        return count


if __name__ == "__main__":
    a = '00000000000000000000000000001011'
    print(set(a))