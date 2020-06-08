# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.record = 0
        self.totalSum = 0
        self.sum = 0
    
    def calNodeSum(self, root, totalSum):
        if root:
            totalSum += root.val
            if totalSum == self.sum:
                self.record += 1
            self.calNodeSum(root.left, totalSum)
            self.totalSum = 0
            self.calNodeSum(root.right, totalSum)


    def preorderTraversal(self, root):
        if root:
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
            totalSum = 0
            self.calNodeSum(root, totalSum)


    def pathSum(self, root, value):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.sum = value
        self.preorderTraversal(root)
        
        return self.record


if __name__ == "__main__":
    # n1 = TreeNode(10)
    # n2 = TreeNode(5)
    # n3 = TreeNode(-3)
    # n4 = TreeNode(3)
    # n5 = TreeNode(2)
    # n6 = TreeNode(11)
    # n7 = TreeNode(3)
    # n8 = TreeNode(-2)
    # n9 = TreeNode(1)
    # n1.left = n2 
    # n1.right = n3
    # n2.left = n4
    # n2.right = n5
    # n3.right = n6
    # n4.left = n7 
    # n4.right = n8
    # n5.right = n9
    n1 = TreeNode(1)
    S = Solution()
    print(S.pathSum(n1, 1))