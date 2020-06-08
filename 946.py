# -*- coding: utf-8 -*-


class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        pushed_length = len(pushed)
        popped_length = len(popped)
        pushed_index = 0
        popped_index = 0
        record_stack = list()

        while pushed_index < pushed_length and popped_index < popped_length:
            while pushed_index < pushed_length and pushed[pushed_index] != popped[popped_index]:
                record_stack.append(pushed[pushed_index])
                pushed_index += 1
            pushed_index += 1
            popped_index += 1
            
            while popped_index < popped_length and record_stack and popped[popped_index] == record_stack[-1]:
                record_stack.pop(-1)
                popped_index += 1

        if record_stack:
            return False
        else:
            return True


if __name__ == "__main__":
    pushed = [1,2,3,4,5]
    popped = [4,3,5,1,2]
    S = Solution()
    print(S.validateStackSequences(pushed, popped))