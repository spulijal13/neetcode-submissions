# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        if length == 1:
            return None

        print(length)
        length -= n
        print(length)

        if length == 0:
            temp = head.next
            head.next = 0
            return temp
        current = head
        while length != 1:
            print(current.val)
            current = current.next
            length -= 1
        
        print(current.val)
        current.next = current.next.next

        return head