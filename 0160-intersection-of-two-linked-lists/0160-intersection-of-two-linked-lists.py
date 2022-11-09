# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ret = None
        start1 = headA
        while start1.next:
            start1.val *= -1
            #print(start1.val)
            start1 = start1.next
        if start1:
            start1.val *= -1
        start2 = headB
        while start2.next:
            if start2.val < 0:
                ret = start2
                break
            else:
                start2 =start2.next
        if ret is None and start2:
            if start2.val < 0:
                ret = start2
        start1 = headA
        while start1.next:
            start1.val *= -1
            start1 = start1.next
        if start1:
            start1.val *= -1
        return ret
                
        