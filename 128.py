# -*- coding: utf-8 -*-


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums_set = set(nums)
        max_num = 0
        count_num = 1

        for num in nums:
            if num in nums_set:
                count_num = 1
                temp_num = num
                remove_set = set()
                remove_set.add(temp_num)
                while (temp_num - 1) in nums_set:
                    temp_num -= 1
                    remove_set.add(temp_num)
                    count_num += 1
                
                temp_num = num
                while (temp_num + 1) in nums_set:
                    temp_num += 1
                    remove_set.add(temp_num)
                    count_num += 1
                                
                if count_num > max_num:
                    max_num = count_num

                if remove_set:
                    for i in remove_set:
                        nums_set.remove(i)
                        
        return max_num


if __name__ == "__main__":
    a = [100, 4, 200, 1, 3, 2]
    S = Solution()
    print(S.longestConsecutive(a))