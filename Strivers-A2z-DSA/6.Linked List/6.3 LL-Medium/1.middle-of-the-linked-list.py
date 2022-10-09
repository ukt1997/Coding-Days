# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        else:
            one = head
            two = head
            while two is not None and two.next is not None:
                two = two.next
                if two.next is not None:
                    two = two.next
                one = one.next
                print(one.val, two.val)

            return one

