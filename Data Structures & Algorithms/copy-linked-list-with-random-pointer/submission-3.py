"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        dummy = Node(0, None, None)
        newCurr = dummy
        oldCurr = head

        while oldCurr:
            newCurr.next = Node(oldCurr.val, None, None)
            newCurr = newCurr.next

            nodes[oldCurr] = newCurr
            oldCurr = oldCurr.next
        
        newHead = dummy.next

        oldCurr = head
        newCurr = newHead

        while oldCurr:
            newCurr.random = nodes.get(oldCurr.random)
            oldCurr = oldCurr.next
            newCurr = newCurr.next
        
        return newHead

            