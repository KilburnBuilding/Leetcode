# -*- coding: utf-8 -*-


class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        t1Length = len(name)
        t2Length = len(typed)
        if t2Length < t1Length:
            return False
        
        tempStack = list()
        i = 0
        j = 0

        while i < t1Length and j < t2Length:
            if name[i] == typed[j]:
                tempStack.append(typed[j])
                i += 1
                j += 1
            else:
                if tempStack:
                    if typed[j] == tempStack[-1]:
                        j += 1
                        continue
                    else:
                        return False
                else:
                    return False

        if ''.join(tempStack) != name:
            return False
        else:
            return True


if __name__ == "__main__":
    name = "sxrmc"
    typed = "sxxrrmmc"
    S = Solution()
    print(S.isLongPressedName(name, typed))
        