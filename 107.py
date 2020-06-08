# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        tempQueue = list()
        finalResult = list()
        if root:
            tempQueue.append(root)
            finalResult.insert(0, [root.val])
        while tempQueue:
            tempResult = list()
            result = list()
            while tempQueue:
                tempResult.append(tempQueue.pop(0))
            for tempNode in tempResult:
                if tempNode.left:
                    tempQueue.append(tempNode.left)
                    result.append(tempNode.left.val)
                if tempNode.right:
                    tempQueue.append(tempNode.right)
                    result.append(tempNode.right.val)
            if result:
                finalResult.insert(0, result)
    
        return finalResult
            

if __name__ == "__main__":
    query_time = 0
    while True:
        query_time += 1
        if query_time > 2:
            print(query_time)
            break
        try:
            print("hahahah")
        except Exception as e:
            if query_time >= 2:
                print("!!!!!!!!!")
            else:
                print("2312321321")