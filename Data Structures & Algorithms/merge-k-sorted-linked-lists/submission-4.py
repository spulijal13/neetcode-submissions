# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Do each solution, 
        # look through each value in the list O(n * k) and O(1)
        # minheap O(nlog(k)) and O(k)
        # merge lists one by one together O(nlog(k)) and O(1)

        k = len(lists)

        if k == 0:
            return None
        
        offset = 1

        while offset < k:
            for i in range(0, k - offset, offset * 2):
                lists[i] = self.merge(lists[i], lists[i + offset])
            
            offset *= 2
        
        return lists[0]

            
    
    def merge(self, head1: ListNode, head2: ListNode) -> ListNode:
        temp1 = head1
        temp2 = head2
        dummy = ListNode(-1)
        check = dummy

        while temp1 and temp2:
            if temp1.val < temp2.val:
                check.next = temp1
                temp1 = temp1.next
            else:
                check.next = temp2
                temp2 = temp2.next
            
            check = check.next
        
        while temp1:
            check.next = temp1
            temp1 = temp1.next 
            check = check.next
        
        while temp2:
            check.next = temp2
            temp2 = temp2.next
            check = check.next
        
        return dummy.next
        
    
    def printList(self, node: ListNode) -> None:
        temp = node

        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        
        print()