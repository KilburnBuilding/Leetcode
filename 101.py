# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def compare(self, root_left, root_right):
        if root_left is None and root_right is None:
            return True
        if (root_left is None and root_right is not None) or (root_left is not None and root_right is None):
            return False
        if root_left is not None and root_right is not None:
            if root_left.val == root_right.val:
                return self.compare(root_left.left, root_right.right) and self.compare(root_left.right, root_right.left)
            else:
                return False
    

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            result = self.compare(root.left, root.right)
        else:
            result = True

        return result
        

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(2)
    n4 = TreeNode(2)
    n5 = TreeNode(2)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n5
    S = Solution()
    print(S.isSymmetric(n1))