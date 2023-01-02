# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseGroup(self,start,end):
        """
        This Function will Reverse the List (Start---> End to End --> Start )
        """
        print("Initial Val " , start.val,end.val)
        head = start
        while start.next != end :
            temp = start.next
            start.next = temp.next
            temp.next = head
            head = temp  
        end.next = head
        start.next = None
        return end,start
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        count = 1
        start = head
        end = head
        prev_end = start
        while end.next :
            count += 1
            end = end.next
            # Use Counter to Check If a group of K elements is formed
            if count%k == 0:
                print("New Bucket")
                temp = end.next
                # Use Counter to Check If a group of K elements is formed if Yes
                # call Reverse function with start, end 
                start,end = self.reverseGroup(start,end)
                print(start.val,end.val)
                if count == k:
                    # Reset Head to 1st start after Reversing 1st K item Subset 
                    head = start
                else:
                    # else just add Start to the end of revesed List formed so far by adding next to previous end 
                    prev_end.next = start
                prev_end = end # Updating Previous end (i.e end of reversed list so far )
                end.next = temp
                start = end.next  # Updating Start to next item 
            
            
        return head
        
        