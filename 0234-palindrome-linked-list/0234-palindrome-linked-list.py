# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:  
    def rev(self,start):
        if start is None or start.next is None:
            return start
        prev_start = start
        while start.next:
            temp = start.next
            start.next = start.next.next
            temp.next = prev_start
            prev_start = temp
        return prev_start
            
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True
        slow = head
        fast = head
        while fast.next and  fast.next.next :
            fast = fast.next.next
            slow = slow.next
            print(fast.val,slow.val)
        mid = slow.next
        print("mid Val",mid.val)
        mid=self.rev(mid)
        """while head:
            print(head.val)
            head = head.next"""
        while mid :
            if head.val != mid.val:
                return False
            head=head.next
            mid = mid.next
        return True
        
            
        
        
        
            
            
            
        