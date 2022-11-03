# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head :
            return
        else:
            start = head
            n = 1
            while start.next :
                start = start.next
                n += 1
            print(n)
            rotate_right = k%n
            splitPos = n - rotate_right
            print(splitPos)
            start = head
            n = 1
            while n < splitPos :
                start = start.next
                n += 1
            if start.next:
                temp = start.next
                start.next = None
                start = temp
                print(start.val)
                while start.next:
                    start = start.next
                start.next = head
                return temp
            else:
                return head
            
        
        