# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = None
        last = None
        total = []
        curVal = 0
        while l1 or l2:
            if l1:
                curVal += l1.val
                l1 = l1.next
            if l2:
                curVal += l2.val
                l2 = l2.next
            total.append(curVal)
            curNode = ListNode(curVal%10)
            curVal = curVal//10
            print(curVal)
            if ret:
                last.next = curNode
                last = last.next
            else:
                ret = curNode
                last = curNode
            
        while curVal > 0:
            curNode = ListNode(curVal%10)
            curVal = curVal//10
            total.append(curVal)
            print(total)
            if ret:
                last.next = curNode
                last = last.next
            else:
                ret = curNode
                last = curNode
                
        return ret
                
            
            
        