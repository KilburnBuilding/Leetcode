# -*- coding: utf-8 -*-


class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        root = -1
        isChild = dict()
        for i in range(n):
            isChild[i] = 0
        for i in leftChild:
            if i == -1:
                continue
            isChild[i] += 1
        for i in rightChild:
            if i == -1:
                continue
            isChild[i] += 1

        rootNumber = 0
        for k, v in isChild.items():
            if v == 0:
                rootNumber += 1
                root = k 

        if rootNumber != 1:
            return False

        queueNode = list()
        queueNode.append(root)
        visit = dict()
        for i in range(n):
            visit[i] = 0
        visit[root] = 1

        while queueNode:
            tempNode = queueNode.pop()
            leftValue = leftChild[tempNode]
            rightValue = rightChild[tempNode]
            if leftValue != -1:
                if visit[leftValue] == 1:
                    return False
                else:
                    queueNode.append(leftValue)
                    visit[leftValue] = 1
            if rightValue != -1:
                if visit[rightValue] == 1:
                    return False
                else:
                    queueNode.append(rightValue)
                    visit[rightValue] = 1
        
        for i in range(n):
            if visit[i] == 0:
                return False
    
        return True


if __name__ == "__main__":
    n = 4
    leftChild = [1, 2, 0, -1]
    rightChild = [-1, -1, -1, -1]
    S = Solution()
    print(S.validateBinaryTreeNodes(n, leftChild, rightChild))
