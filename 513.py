# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        
        if not root.left and root.right:
            return root.val

        firstLevel = list()
        firstLevel.append(root)
        secondLevel = list()
        leftValue = 0
        firstEmpty = False
        while len(firstLevel) != 0:
            tempNode = firstLevel.pop(0)
            if tempNode.left:
                secondLevel.append(tempNode.left)
            if tempNode.right:
                secondLevel.append(tempNode.right)
            if not firstLevel:
                firstEmpty = True
            if firstEmpty and secondLevel:
                leftValue = secondLevel[0].val
                firstLevel = list(secondLevel)
                secondLevel = list()
                firstEmpty = False
        
        return leftValue


if __name__ == "__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t3.left = t5
    t3.right = t6
    t5.left = t7
    S = Solution()
    print(S.findBottomLeftValue(t1))
            
