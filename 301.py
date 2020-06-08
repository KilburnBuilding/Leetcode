# -*- coding: utf-8 -*-


class Solution(object):
    def __init__(self):
        self.result = set()
        self.minNumber = float('inf')

    def isRight(self, record):
        result = list()
        for i in record:
            if i == '(':
                result.append(i)
            if i == ')':
                if result and result[-1] == '(':
                    result.pop(-1)
                else:
                    result.append(')')
        if result:
            return False
        else:
            return True

    def backtrack(self, record, index, number):
        if ('(' not in record and ')' not in record) or not record:
            return
        else:
            if self.isRight(record):
                if number == self.minNumber:
                    self.result.add(''.join(record))
                if number < self.minNumber:
                    self.minNumber = number
                    self.result = set()
                    self.result.add(''.join(record))
    
            length = len(record)
            for i in range(index + 1, length):
                if record[i] == '(' or record[i] == ')':
                    record[i] = ''
                    number += 1
                    self.backtrack(record, i, number)                  

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = list()
        record = list()
        length = len(s)
        if not s:
            result.append("")
            return result

        else:
            for i in s:
                record.append(i)
            
            if self.isRight(record):
                result.append(''.join(record))
                return result
            
            for i in range(length):
                 if record[i] == '(' or record[i] == ')':
                    temp = list(record)
                    temp[i] = ''
                    self.backtrack(temp, i, 1)
                    temp = list(record)

        if not self.result:
            temp_result = list()
            for i in s:
                if i != '(' and i != ')':
                    temp_result.append(i)
            result.append(''.join(temp_result))
        else:
            result = list(self.result)

        return result


if __name__ == "__main__":
    s = ")()("
    S = Solution()
    print(S.removeInvalidParentheses(s))