class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        sStack = list()
        tStack = list()

        for s in S:
            if s != '#':
                sStack.append(s)
            else:
                if sStack:
                    sStack.pop(-1)
        for t in T:
            if t != '#':
                tStack.append(t)
            else:
                if tStack:
                    tStack.pop(-1)

        if ''.join(sStack) == ''.join(tStack):
            return True
        else:
            return False
        

if __name__ == "__main__":
    S = Solution()
    s1 = "ab#c"
    t1 = "ad#c"
    s2 = "ab##"
    t2 = "c#d#"
    s3 = "a##c"
    t3 = "#a#c" 
    s4 = "a#c"
    t4 = "b"
    print(S.backspaceCompare(s4, t4))