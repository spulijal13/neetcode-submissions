# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp1 = l1
        temp2 = l2
        totalOne = 0
        totalTwo = 0
        mult = 1
        while temp1 or temp2:
            if temp1 == None:
                oneVal = 0
            else:
                oneVal = temp1.val
                temp1 = temp1.next
            
            if not temp2:
                twoVal = 0
            else:
                twoVal = temp2.val
                temp2 = temp2.next
            
            totalOne += oneVal * mult
            totalTwo += twoVal * mult
            mult *= 10
        
        print(totalOne, totalTwo)
        sumVal = totalOne + totalTwo

        if sumVal == 0:
            return ListNode()

        head = None
        while sumVal != 0:
            if not head:
                head = ListNode(sumVal % 10)
                temp = head
            else:
                temp.next = ListNode(sumVal % 10)
                temp = temp.next
            sumVal = sumVal // 10
        
        return head