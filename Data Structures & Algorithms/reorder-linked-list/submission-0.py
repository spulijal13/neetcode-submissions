# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None:
            return
        

        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        part = length // 2 - 1 if length % 2 == 0 else length // 2
        print(part)
        temp = head
        while part != 0:
            temp = temp.next
            part -= 1
        half = temp.next
        temp.next = None
        print(temp.val)

        currNode = half
        prevNode = None
        while currNode:
            placeholder = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = placeholder
        
        half = prevNode
        node = head

        while half:
            temp1 = node.next
            temp2 = half.next

            node.next = half
            half.next = temp1

            node = temp1
            half = temp2
        
