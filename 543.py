# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.maxDeepth = 0

    def process(self, root):
        if not root:
            return 0

        leftDeepth = self.process(root.left)
        rightDeepth = self.process(root.right)
        
        if (leftDeepth + rightDeepth) >= self.maxDeepth:
            self.maxDeepth = leftDeepth + rightDeepth
        
        if leftDeepth > rightDeepth:
            return leftDeepth + 1
        else:
            return rightDeepth + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.process(root)
        return self.maxDeepth


if __name__ == "__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    S = Solution()
    print(S.diameterOfBinaryTree(t1))
    