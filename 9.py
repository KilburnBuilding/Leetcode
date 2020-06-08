# -*- coding: utf-8 -*-


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    a = 12
    b = 12
    print(a^b)
    