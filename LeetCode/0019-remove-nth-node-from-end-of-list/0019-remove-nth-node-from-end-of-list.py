# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        cur = head
        for i in range(n):
            end = end.next
        if end is None:
            return head.next
        while end.next is not None:
            print(cur.val,end.val)
            end = end.next
            cur = cur.next
        cur.next = cur.next.next
        return head
        