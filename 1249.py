# -*- coding: utf-8 -*-


class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        recordStack = list()
        result = list()

        for k, v in enumerate(s):
            if v != ')' and v != '(':
                result.append(v)
            else:
                result.append('')
                if recordStack:
                    if recordStack[-1][0] == '(' and  v == ')':
                        value = recordStack.pop(-1)
                        result[value[1]] = value[0]
                        result[k] = v
                    else:
                        recordStack.append([v, k])
                else:
                    recordStack.append([v, k])
        
        return ''.join(result)


if __name__ == "__main__":
    s = "))(("
    S = Solution()
    print(S.minRemoveToMakeValid(s))