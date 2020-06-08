# -*- coding: utf-8 -*-


class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        record_stack = list()

        for i in S:
            if i == '(':
                record_stack.append(i)
            else:
                temp_sum = 0
                while record_stack[-1] != '(':
                    temp_sum += record_stack.pop(-1)
                record_stack.pop(-1)
                if temp_sum == 0:
                    record_stack.append(1)
                else:
                    record_stack.append(2 * temp_sum)

            print(record_stack)

        return sum(record_stack)


if __name__ == "__main__":
    M = "(()(()))"
    S = Solution()
    print(S.scoreOfParentheses(M))