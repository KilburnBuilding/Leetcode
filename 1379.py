# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def solve(self, original, cloned, target):
        if not original:
            return
        if original == target:
            return cloned
        return self.solve(original.left, cloned.left, target) or self.solve(original.right, cloned.right, target)

    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        return self.solve(original, cloned, target)
        




        