# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        currNode = head
        count = 0
        ListNode.index = -1

        while currNode != None:
            if currNode.index == -1:
                currNode.index = count
                count += 1
            else:
                return True
            currNode = currNode.next

        
        return False