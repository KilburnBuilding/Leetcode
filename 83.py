# -*- coding: utf-8 -*-
import copy


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
    
        FirstNode = ListNode(-1)
        FirstNode.next = head
        tempResult = head.val
        tempNode = head.next

        while head:
            tempNode = head.next
            if tempNode:
                if tempNode.val == tempResult:
                    head.next = tempNode.next
                else:
                    tempResult = tempNode.val
                    head = head.next
            else:
                break

        return FirstNode.next


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(1)
    n3 = ListNode(2)
    n4 = ListNode(3)
    n5 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    S = Solution()
    tempNode = S.deleteDuplicates(n1)

    while tempNode:
        print(tempNode.val)
        tempNode = tempNode.next