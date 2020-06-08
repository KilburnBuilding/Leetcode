# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if (root.val >= q.val and root.val <= p.val) or (root.val >= p.val and root.val <= q.val):
            return root
        if root.val >= p.val and root.val >= q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        

if __name__ == "__main__":
    n1 = TreeNode(6)
    n2 = TreeNode(2)
    n3 = TreeNode(8)
    n4 = TreeNode(0)
    n5 = TreeNode(4)
    n6 = TreeNode(7)
    n7 = TreeNode(9)
    n8 = TreeNode(3)
    n9 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n5.left = n8
    n5.right = n9
    S = Solution()
    value = S.lowestCommonAncestor(n1, n2, n3)
    print(value.val)