# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def middleSequence(self, t1, t2):
        if t1 and t2:
            t1.val = t1.val + t2.val
            self.middleSequence(t1.left, t2.left)
            self.middleSequence(t1.right, t2.right)
        if t1 and not t2:
            self.middleSequence(t1.left, None)
            self.middleSequence(t1.right, None)
        if not t1 and t2:
            t1 = t2
            self.middleSequence(t1.left, None)
            self.middleSequence(t1.right, None)

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        temp_node = t1
        self.middleSequence(t1, t2)
        return temp_node


if __name__ == "__main__":
    t10 = TreeNode(1)
    t11 = TreeNode(3)
    t12 = TreeNode(2)
    t13 = TreeNode(5)
    t10.left = t11
    t10.right = t12
    t11.left = t13

    t20 = TreeNode(2)
    t21 = TreeNode(1)
    t22 = TreeNode(3)
    t23 = TreeNode(4)
    t24 = TreeNode(7)
    t20.left = t21
    t20.right = t22
    t21.right = t23
    t22.right = t24

    S = Solution()
    S.mergeTrees(t10, t20)