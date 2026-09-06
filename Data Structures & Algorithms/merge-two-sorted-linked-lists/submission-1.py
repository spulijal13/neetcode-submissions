# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = None
        while list1 or list2:
            if not list1:
                next_node = list2
                list2 = list2.next
            elif not list2:
                next_node = list1
                list1 = list1.next
            else:
                if list1.val < list2.val:
                    next_node = list1
                    list1 = list1.next
                else:
                    next_node = list2
                    list2 = list2.next
            
            print(next_node)
            
            if not head:
                head = next_node
                temp = head
            else:
                temp.next = next_node
                temp = temp.next
        
        return head

            
                