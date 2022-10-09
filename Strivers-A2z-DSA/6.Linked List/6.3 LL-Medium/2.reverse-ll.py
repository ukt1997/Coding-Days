# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        last = None
        while head.next is not None:
            next_n = head.next
            head.next = last
            last = head
            head = next_n
        head.next = last
        return head



