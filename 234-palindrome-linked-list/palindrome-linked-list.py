# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head.next is None:
            return True
        slow,fast = head,head
        while fast.next is not  None and fast.next.next is not None:
            slow = slow.next
            fast=fast.next.next
        mid = slow 
        cur,prev = slow.next,None
        while cur is not None:
           temp = cur.next
           cur.next = prev
           prev = cur
           cur = temp
        while prev is not None:
            if head.val!=prev.val:
                return False
            head = head.next
            prev=prev.next
        return True

        