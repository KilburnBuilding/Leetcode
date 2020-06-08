# -*- coding: utf-8 -*-


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = list()
        window_result = list()
        index = 0
        temp_count = 0

        if not nums:
            return result
        
        length = len(nums)


        while index < length:
            temp_count += 1
            if temp_count < k:
                if not window_result:
                    window_result.insert(0, nums[index])
                else:
                    if nums[index] > window_result[0]:
                        window_result[0] = nums[index]
                    else:
                        add_flag = False
                        for j in range(len(window_result)):
                            if nums[index] > window_result[j]:
                                window_result.insert(j, nums[index])
                                add_flag = True
                                break
                        if not add_flag:
                            window_result.append(nums[index])
            elif temp_count == k
                temp_value = window_result[0]
                window_result = list()
                window_result.append(temp_value)
            
            else:
                window_result.pop(0)
            
            index += 1
            print('----------window_result------------')
            print(window_result)
            print('-----------------------------------')


if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    S = Solution()
    print(S.maxSlidingWindow(nums, k))
    
