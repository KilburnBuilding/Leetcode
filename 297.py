# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        first_queue = list()
        second_queue = list()
        result = list()
        if root:
            first_queue.append(root)
            result.append(root.val)
            while first_queue:
                tempNode = first_queue.pop(0)
                if tempNode.left:
                    second_queue.append(tempNode.left)
                    result.append(tempNode.left.val)
                else:
                    result.append('null')

                if tempNode.right:
                    second_queue.append(tempNode.right)
                    result.append(tempNode.right.val)
                else:
                    result.append('null')

                if not first_queue:
                    first_queue = second_queue
                    second_queue = list()

        return str(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


if __name__ == "__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t1.left = t2
    t1.right = t3
    t3.left = t4
    t3.right = t5
    C = Codec()
    print(C.serialize(t1))