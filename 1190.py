# -*- coding: utf-8 -*-


class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [s[0]]

        for i in s[1:]:
            if i == ')':
                tempRecord = list()
                while stack[-1] != '(':
                    tempRecord.append(stack.pop())
                stack.pop()

                for i in tempRecord:
                    stack.append(i)
            else:
                stack.append(i)

        result = list()
        print(stack)
        while stack:
            result.insert(0, stack.pop())

        return ''.join(result)


if __name__ == "__main__":
    s = "(ed(et(oc))el)"
    S = Solution()
    print(S.reverseParentheses(s))
