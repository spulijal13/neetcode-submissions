# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        curr = head
        for _ in range((length - 1) // 2):
            curr = curr.next

        reverse = curr.next
        curr.next = None

        prev = None
        while reverse:
            temp = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = temp
        
        curr = head
        reverse = prev

        while reverse:
            temp1 = curr.next
            temp2 = reverse.next

            curr.next = reverse
            reverse.next = temp1

            curr = temp1
            reverse = temp2