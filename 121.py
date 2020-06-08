# -*- coding: utf-8 -*-


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        int_min = 65535
        int_max = 0
        int_profit = 0
        for i in prices:
            if i < int_min:
                int_min = i
                int_max = int_min
            if i > int_max:
                int_max = i

            if int_profit < int_max - int_min:
                int_profit = int_max - int_min

        return int_profit
        

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    S = Solution()
    S.maxProfit(prices)