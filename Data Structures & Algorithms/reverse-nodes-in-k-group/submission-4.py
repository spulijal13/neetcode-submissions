# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prevTail = dummy
        curr = dummy.next

        while curr:
            count = 0
            check = curr
            
            while check and count < k:
                count += 1
                check = check.next
            
            if count < k:
                break
            
            nextHead = check
            groupHead = curr

            prev = nextHead

            while curr != nextHead:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            prevTail.next = prev

            prevTail = groupHead
            curr = nextHead 
        
        return dummy.next
                
                    





        