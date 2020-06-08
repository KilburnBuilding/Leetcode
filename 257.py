# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.result = list()
        self.tempResult = list()

    def traverTree(self, root):
        if root:
            self.tempResult.append(root.val)
            if not root.left and not root.right:
                if self.tempResult:
                    self.result.append('->'.join(self.tempResult))
            self.binaryTreePaths(root.left)
            self.binaryTreePaths(root.right)
            self.tempResult.pop(-1)

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.traverTree(root)

        return self.result


if __name__ == "__main__":
    t1 = TreeNode('1')
    t2 = TreeNode('2')
    t3 = TreeNode('3')
    t4 = TreeNode('5')
    t1.left = t2
    t1.right = t3
    t2.right = t4
    S = Solution()
    print(S.binaryTreePaths(t1))