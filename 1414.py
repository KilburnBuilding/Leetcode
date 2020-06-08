# -*- coding: utf-8 -*- 


class Solution(object):
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        fn_1 = 1
        fn_2 = 1
        fn = 1
        result = 0
        fibonacc_list = list()
        fibonacc_list.append(1)
        fibonacc_list.append(1)
        
        while fn < k:
            fn_1 = fn_2
            fn_2 = fn
            fn = fn_1 + fn_2
            fibonacc_list.append(fn)
        
        if fibonacc_list[-1] > k:
            fibonacc_list.pop(-1)
        
        while k > 0:
            k = k - fibonacc_list.pop(-1)

            while len(fibonacc_list) > 0 and fibonacc_list[-1] > k:
                fibonacc_list.pop(-1)

            result += 1

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.findMinFibonacciNumbers(10))