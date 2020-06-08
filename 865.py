# -*- coding: utf-8 -*-



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def depth(self, root):
        if not root:
            return [-1, None]
        l = self.depth(root.left)
        r = self.depth(root.right)
        dl = l[0]
        dr = r[0]

        if dl == dr:
            tempResult = root
        else:
            if dl > dr:
                tempResult = l[1]
            else:
                tempResult = r[1]

        return [max(dl, dr) + 1, tempResult]


    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.depth(root)[1]

              


if __name__ == "__main__":
    t1 = TreeNode(3)
    t2 = TreeNode(5)
    t3 = TreeNode(1)
    t4 = TreeNode(6)
    t5 = TreeNode(2)
    t6 = TreeNode(0)
    t7 = TreeNode(8)
    t8 = TreeNode(7)
    t9 = TreeNode(4)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    t5.left = t8
    t5.right = t9
    S = Solution()
    t = S.subtreeWithAllDeepest(t1)
    print(t.val)