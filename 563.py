# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.sumValue = 0

    def traverseNode(self, root):
        if not root:
            return 0
        leftValue = self.traverseNode(root.left)
        rightValue = self.traverseNode(root.right)
        self.sumValue += abs(leftValue - rightValue)

        return leftValue + rightValue + root.val
        
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traverseNode(root)

        return self.sumValue
        

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left = n2
    n1.right = n3 
    n2.left = n4
    n3.left = n5
    S = Solution()
    print(S.findTilt(n1))