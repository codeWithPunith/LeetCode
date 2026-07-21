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
        if head is None or head.next is None :
            return True
        slow,fast = head,head
        while fast.next is not None and fast.next.next is not None :
            slow = slow.next
            fast=fast.next.next
        BeginingOfSecond = slow.next

        prev = None
        while BeginingOfSecond is not None:
            temp = BeginingOfSecond.next
            BeginingOfSecond.next= prev
            prev =BeginingOfSecond
            BeginingOfSecond=temp
        while prev:
            if prev.val!=head.val:
                return False
            head=head.next
            prev=prev.next
        return True
        