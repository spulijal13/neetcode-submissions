# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        heap = []

        for i in range(k):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        
        if not heap:
            return None
        
        head = None
        while heap:
            value, index = heapq.heappop(heap)

            if not head:
                head = ListNode(value)
                temp = head
            else:
                temp.next = ListNode(value)
                temp = temp.next

            if lists[index]:
                heapq.heappush(heap, (lists[index].val, index))
                lists[index] = lists[index].next
            

        

        return head
                