# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = list()

        if not head:
            return True

        temp_node = head
        while temp_node:
            stack.append(temp_node.val)
            temp_node = temp_node.next
        
        while stack and head:
            stack_val = stack.pop(-1)
            head_val = head.val

            if stack_val != head_val:
                return False
            head = head.next
        
        return True 


if __name__ == "__main__":
    t1 = ListNode(1)
    t2 = ListNode(2)
    t3 = ListNode(2)
    t4 = ListNode(1)
    t1.next = t2
    t2.next = t3
    t3.next = t4
    
    S = Solution()
    print(S.isPalindrome(t1))