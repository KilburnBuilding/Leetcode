# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode(-1)
        temp = root
        while l1 and l2:
            if l1.val <= l2.val:
                root.next = l1
                root = root.next
                l1 = l1.next
            else:
                root.next = l2
                root = root.next
                l2 = l2.next

        if l1:
            root.next = l1
        if l2:
            root.next = l2
        
        return temp.next


if __name__ == "__main__":
    t1 = ListNode(1)
    t2 = ListNode(2)
    t3 = ListNode(4)
    t1.next = t2
    t2.next = t3
    l1 = ListNode(1)
    l2 = ListNode(3)
    l3 = ListNode(4)
    l1.next = l2
    l2.next = l3
    S = Solution()
    result = S.mergeTwoLists(t1, l1)
    while result:
        print(result.val)
        result = result.next




