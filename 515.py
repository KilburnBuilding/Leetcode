# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        firstLevel = list()
        secordLevel = list()
        levelValue = list()
        maxValue = list()
        firstLevel.append(root)
        if not root:
            return maxValue

        while firstLevel:
            tempNode = firstLevel.pop(0)
            levelValue.append(tempNode.val)
            if tempNode.left:
                secordLevel.append(tempNode.left)
            if tempNode.right:
                secordLevel.append(tempNode.right)

            if not firstLevel:
                firstLevel = list(secordLevel)
                maxValue.append(max(levelValue))
                secordLevel = list()
                levelValue = list()

        return maxValue


if __name__ == "__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(3)
    t3 = TreeNode(2)
    t4 = TreeNode(5)
    t5 = TreeNode(3)
    t6 = TreeNode(9)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.right = t6
    S = Solution()
    print(S.largestValues(t1))
