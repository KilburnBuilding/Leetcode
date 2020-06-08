# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameNode(self, s, t):
        if s and t and s.val == t.val:
            return self.isSameNode(s.right, t.right) and self.isSameNode(s.left, t.left)
        if not s and not t:
            return True
        if (not s and t) or (s and not t):
            return False 

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        if (not s and t) or (s and not t):
            return False
        if s and t:
            return self.isSameNode(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
            

        
if __name__ == "__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(1)
    # t3 = TreeNode(5)
    # t4 = TreeNode(1)
    # t5 = TreeNode(2)
    # t6 = TreeNode(0)
    t1.left = t2
    # t1.right = t3
    # t2.left = t4
    # t2.right = t5
    # t5.right = t6

    r1 = TreeNode(1)
    # r2 = TreeNode(1)
    # r3 = TreeNode(2)
    # r1.left = r2
    # r1.right = r3
    S = Solution()
    print(S.isSubtree(t1, r1))
