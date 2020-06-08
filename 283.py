class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp_stack = list()
        for i in nums:
            if i == 0:
                i = ''
                count += 1
        
        
            
        

if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    nums.remove(0)
    print(nums)
    # S = Solution()
    # S.moveZeroes(nums)