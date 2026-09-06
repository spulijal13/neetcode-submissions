# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2

        if list2 == None:
            return list1

        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        currNode = head
        
        while list1 != None and list2 != None:
            
            if list1.val < list2.val:
                currNode.next = list1
                list1 = list1.next
            else:
                currNode.next = list2
                list2 = list2.next
            
            currNode = currNode.next

        if list1 is not None:
            currNode.next = list1
        else:
            currNode.next = list2

        return head

            
                