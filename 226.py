# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
        

if __name__ == "__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t4 = TreeNode(4)
    t7 = TreeNode(7)
    t4.left = t2
    t4.right = t7
    t2.left = t1
    S = Solution()
    S.invertTree(t4)
