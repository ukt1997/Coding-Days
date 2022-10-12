# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        if head.next is None:
            return None
        else:
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            print(fast.val,slow.val)
            if fast.next:
                slow.next = slow.next.next
            else:
                slow.val = slow.next.val
                slow.next = slow.next.next
            return head
        