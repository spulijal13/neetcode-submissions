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

        dummy = ListNode(-1)
        temp = dummy
        heap = []
        k = len(lists)

        for i in range(k):
            if lists[i]:
                heap.append((lists[i].val, i))
        
        heapq.heapify(heap)

        while True:
            if not heap:
                break
            
            minVal, minInd = heapq.heappop(heap)
            temp.next = lists[minInd]
            lists[minInd] = lists[minInd].next
            temp = temp.next
            temp.next = None

            if lists[minInd]:
                heapq.heappush(heap, (lists[minInd].val, minInd))


        return dummy.next
    
    def printList(self, node: ListNode) -> None:
        temp = node

        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        
        print()